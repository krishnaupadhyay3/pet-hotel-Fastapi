from .models import LoginUser, Token , UserInDB , TokenData, User , \
InviteEmail, UserInput, UserCommon , PetDetails , PetUpdate
from .models import  PetList , PetClass , PetInDB

from .api_exceptions import invalid_data_exception , credentials_exception , \
inactive_user , invalid_post_data , not_permitted , not_found , existing_user
from .utils import get_password_hash, verify_password ,\
 create_compaign_user , send_transaction_email
from .config import ACCESS_TOKEN_EXPIRE_MINUTES, ADMIN_EMAIL, ADMIN_PASS, ADMIN_USER ,\
DATABASE_NAME, SECRET_KEY , ALGORITHM

from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends , status
from fastapi.encoders import jsonable_encoder

from jose import JWTError, jwt
import motor.motor_asyncio
from starlette.responses import Response
from typing import List , Optional

app = FastAPI()


client = motor.motor_asyncio.AsyncIOMotorClient("mongodb",27017)
database = client[DATABASE_NAME]
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/v1/token")

    

async def get_user(db, username: str):
    user_result = await database["users"].find_one({"username":username })

    if username in user_result.get("username"):
        if user_result.get("disabled"):
            raise inactive_user
        return UserInDB(**user_result)


async def authenticate_user(fake_db, username: str, password: str):
    user = await get_user(fake_db, username)

    if not user:
        return False
    if not verify_password(password, user.password):

        login_attempt = user.login_attempt +1 
        if login_attempt > 3 :
            await database["users"].update_one({"username":username},{
                "$set":{"disabled":True}})

            raise inactive_user

        await database["users"].update_one({"username":username},{"$set":{"login_attempt":login_attempt}})

        return False
    return user

async def get_pet_details(databse ,pet_id:str , role:str , current_user:str):
    db_query = {"pet_name":pet_id}
    if role == "customer" :
        db_query ["owner"] = current_user
        db_query["checked_in"] = False
    result = await database["pets"].find_one(db_query,{"_id":0})
    return jsonable_encoder(result)



def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(database, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise inactive_user
    return current_user
        
class RoleChecker:
    def __init__(self, allowed_roles: List):
        self.allowed_roles = allowed_roles

    def __call__(self, user: User = Depends(get_current_active_user)):
        if user.roles not in self.allowed_roles:
            raise not_permitted
        return User
        


allow_manager_staff =  RoleChecker(["staff","manager"])
allow_admin = RoleChecker(["admin"])

### api started

@app.on_event("startup")
async def create_db_client():
    user_collection = database["users"]
    is_admin = await user_collection.find_one({"username":ADMIN_USER })

    if not is_admin :
        admin_dict = {"username":ADMIN_USER ,"email":ADMIN_EMAIL ,
        "password":get_password_hash(ADMIN_PASS),"fullname":"admin","roles":"admin"}
        user_collection.insert_one(admin_dict)



@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()

@app.post("/v1/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    
    user = await authenticate_user(database, form_data.username, form_data.password)
    print(user)
    if not user:
        raise invalid_data_exception

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}




@app.post("/v1/register")
async def create_common_user(user :UserCommon , response:Response):
    dict_data = jsonable_encoder(user)
    is_user = await database["users"].find_one({"username":dict_data["username"]})
    if is_user :
        raise existing_user
    dict_data["password"] = get_password_hash(dict_data["password"])
    dict_data = jsonable_encoder(User(**dict_data))
    create_user  = await database["users"].insert_one(dict_data)
    response.status_code = status.HTTP_201_CREATED
    return {"status" :"created successfully"}



@app.get("/v1/pet" , response_model=List[PetList])
async def list_pet(skip: int = 0, limit: int = 10,current_user: User = Depends(get_current_active_user)):

    pets_result =  database["pets"].find({"owner":current_user.username}).skip(skip).limit(limit)
    pet_result =  await pets_result.to_list(length=limit)
    return pet_result

@app.post("/v1/pet")
async def pet_create(pet_data:PetClass , response:Response,
               current_user: User = Depends(get_current_active_user) ):
    pet_data = jsonable_encoder(pet_data)

    pet_data["owner"] = current_user.username
    pet_Data  = PetInDB(**pet_data)
    pet_Data = jsonable_encoder(pet_Data)
    pets_result = await database["pets"].insert_one(pet_Data)
    if pets_result :
        response.status_code = status.HTTP_201_CREATED
        return {"status":"pet_created"}
    response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    return {"status":"error occured "}

@app.delete("/v1/pet/{pet_id}")
async def pet_delete(pet_id:str,response:Response,current_user: User = Depends(get_current_active_user)):

    if current_user.roles == "manager":
        pets = await database["pets"].delete_one({"pet_name":pet_id })
    elif current_user.roles == "customer" :
        pets = await database["pets"].find_one({"pet_name":pet_id,"checked_in":False ,
                                            "owner":current_user.username})
        if pets :
            await database["pets"].delete_one({"pet_name":pet_id,"checked_in":False ,
                                            "owner":current_user.username})
        else:
            raise not_found
    else :
        raise not_permitted
    response.status_code = status.HTTP_204_NO_CONTENT
    return {"status":"deleted successfully"}

@app.get("/v1/pet/{pet_id}")
async def pet_info(pet_id:str, current_user: User = Depends(get_current_active_user)):
    data = await get_pet_details(database ,pet_id=pet_id , 
            role=current_user.roles, current_user=current_user.username)
    if not data :
        raise not_found
    pet_data = PetDetails(current_user.roles, data).get_data()
    return jsonable_encoder(pet_data)

@app.put("/v1/pet/{pet_id}")
async def pet_update(pet_id:str,pet_data:PetInDB ,current_user: User = Depends(get_current_active_user)):

    pet_user_data  = PetUpdate(current_user.roles , pet_data)
    data = await get_pet_details(database ,pet_id=pet_id , 
            role=current_user.roles, current_user=current_user.username)
    if not data :
        raise not_found

    db_update_data = jsonable_encoder(pet_user_data)
    result = await database["pets"].update_one({"username":current_user.username},
                                                {"$set":db_update_data})
    return {"status":"successfully updated "}


@app.post("/v1/invite")
def user_invite(user_mail :InviteEmail , response:Response , 
                current_user: User = Depends(allow_manager_staff)):

    email_address = jsonable_encoder(user_mail)
    if not email_address :
        raise invalid_post_data
    
    if not create_compaign_user(email_address.get("email")) :
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status":"internal server error occured "}

    if not send_transaction_email(email_address.get("email")):
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"status":"internal server error occured "}

    return {"status":"invite send successfully"}



@app.post("/v1/unblock/")
async def unblock_user(user_mail :InviteEmail , response:Response , 
                current_user: User = Depends(allow_manager_staff)):
    email_address = jsonable_encoder(user_mail)
    if not email_address :
        raise invalid_post_data
    result = await database["users"].update_one({"email":email_address.get("email") },
                                                {"$set":{"disabled":False ,"login_attempt":0}})
    
    return {"status":"email {} unblocked".format(email_address.get("email"))}

@app.post("/v1/rootuser")
async def create_user(user :UserInput, response:Response,current_user: User = Depends(allow_admin)) :
    dict_data = jsonable_encoder(user)
    is_user = await database["users"].find_one({"username":dict_data["username"]})
    if is_user :
        raise existing_user
    dict_data["password"] = get_password_hash(dict_data["password"])
    dict_data = jsonable_encoder(User(**dict_data))
    await database["users"].insert_one(dict_data)
    response.status_code = status.HTTP_201_CREATED
    return {"status" :"created successfully"}
