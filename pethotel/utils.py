from passlib.context import CryptContext
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from .config import TRANSACTIONAL_MAIL_KEY , COMPAIGN_ID


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)



def create_compaign_user(user_mail):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = TRANSACTIONAL_MAIL_KEY

    api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))
    create_contact = sib_api_v3_sdk.CreateContact(
    email= user_mail,  list_ids=[COMPAIGN_ID] ) 

    try:
        api_response = api_instance.create_contact(create_contact)
    except ApiException as e:
        print("Exception when calling ContactsApi->create_contact: %s\n" % e)
        return False
    return True

def send_transaction_email(user_mail):
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = TRANSACTIONAL_MAIL_KEY

    api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
    campaign_id = 1
    email_to = sib_api_v3_sdk.SendTestEmail(email_to=[user_mail])

    try:
        resp = api_instance.send_test_email(campaign_id, email_to)
    except ApiException as e:
        print("Exception when calling EmailCampaignsApi->send_test_email: %s\n" % e)
        return False

    return True