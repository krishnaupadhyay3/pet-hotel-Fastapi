from dotenv import load_dotenv
import os
load_dotenv()
#jwt token based 
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

DATABASE_NAME  = os.getenv("DATABASE_NAME")

#site administrator
ADMIN_USER = os.getenv("ADMIN_USER")
ADMIN_PASS = os.getenv("ADMIN_PASS")
ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")


# use sendin blue mail key
TRANSACTIONAL_MAIL_KEY =  os.getenv("TRANSACTIONAL_MAIL_KEY")
COMPAIGN_ID = int(os.getenv("COMPAIGN_ID") )
