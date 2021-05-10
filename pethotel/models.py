from typing import Optional ,List 
from pydantic import BaseModel , EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    email: str 
    full_name: Optional[str]
    password : str
    roles: str = "customer"
    login_attempt : int = 0
    disabled: bool = False

class UserInput(BaseModel) :
    username: str
    email: str 
    full_name: Optional[str]
    password : str
    roles: str = "customer"

class UserCommon(BaseModel):
    username: str
    email: str 
    full_name: Optional[str]
    password : str

class TokenData(BaseModel):
    username: Optional[str] = None
    
class UserInDB(User):
    password: str

class LoginUser(BaseModel):
    username: str
    password : str
    

class PetClass(BaseModel) :
    pet_name :str

class PetInDB(PetClass) :
    checked_in: bool = False
    room : Optional[str] = None 
    deleted : bool =False
    owner :str

class PetList(BaseModel) :
    pet_name : str
    checked_in : str
    room : Optional[str]=None

class PetUpdateMin(BaseModel):
    pet_name: str

class PetUpdateStaff(BaseModel):
    pet_name: str
    checked_in : Optional[bool]= False

class PetUpdateManager(BaseModel):
    pet_name: str
    checked_in : Optional[bool]= False
    room :Optional[str] =None

class InviteEmail(BaseModel):
    email: EmailStr

class PetDetails:
    def __init__(self,roles, data) :
        self.roles = roles 
        self.data = data

    def get_data(self ) :
        if self.roles == "customer":
            
            return PetList(**self.data)
        elif self.roles in[ "staff" ,"manager"] :
            return PetInDB(**self.data)

        else :
            return PetList(**self.data)
class PetUpdate:
    def __init__(self,roles, data) :
        self.roles = roles 
        self.data = data

    def get_data(self ) :
        if self.roles == "customer":
            
            return PetUpdateMin(**self.data)
        elif self.roles == "staff" :
            return PetUpdateStaff(**self.data)
        elif self.roles == "manager" :
            return PetUpdateManager(**self.data)
        else :
            return PetUpdateMin(**self.data)