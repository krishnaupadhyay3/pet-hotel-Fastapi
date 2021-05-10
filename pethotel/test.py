from __future__ import print_function
import time
import datetime
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = 1

# create an instance of the API class
api_instance = sib_api_v3_sdk.ContactsApi(sib_api_v3_sdk.ApiClient(configuration))
create_contact = sib_api_v3_sdk.CreateContact(
  email= 'zolopeha@zetmail.com',  list_ids=[3]
) # CreateContact | Values to create a contact

try:
    # Create a contact
    api_response = api_instance.create_contact(create_contact)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactsApi->create_contact: %s\n" % e)

configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = "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"

api_instance = sib_api_v3_sdk.EmailCampaignsApi(sib_api_v3_sdk.ApiClient(configuration))
campaign_id = 1
email_to = sib_api_v3_sdk.SendTestEmail(email_to=['zolopeha@zetmail.com'])

try:
    resp = api_instance.send_test_email(campaign_id, email_to)
    print(resp)
except ApiException as e:
    print("Exception when calling EmailCampaignsApi->send_test_email: %s\n" % e)

