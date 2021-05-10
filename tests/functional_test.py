import json
import unittest
import requests
class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = requests.session()

    def tearDown(self):  
        self.browser.close()

    def test_1_register_to_pet_hotel(self):  
        # John doe got a Invitation about a cool pet hotel for registration
        # he register at site using {  "username": "string","email": "string",
        # "full_name": "string","password": "string"}
        registration_data = {
                            "username": "john",
                            "email": "johndoe@secret.com",
                            "full_name": "john doe",
                            "password": "john123"
                            }
        resp = self.browser.post('http://localhost:8000/v1/register', json=registration_data)

        self.assertEqual(201, resp.status_code)  
        self.assertEqual({"status": "created successfully"},resp.json())
  
    def test_2_login_to_pet_hotel(self):
        # after registration John doe continue to login to the pet hotel using username 
        # and password

        login_data = {
            "username":"john",
            "password":"john123"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = self.browser.post('http://localhost:8000/v1/token', data=login_data)
        self.assertEqual(200, resp.status_code) 
        
 

    def test_3_creating_and_getting_a_pet(self) :
        # after login John Doe goes to create a pet for himself

        login_data = {
            "username":"john",
            "password":"john123"
        }
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        resp = self.browser.post('http://localhost:8000/v1/token', data=login_data)
        token = resp.json().get("access_token")

        pet_data = {"pet_name":"fluffy"}       
        hed = {'Authorization': 'Bearer ' + token} 
        resp = self.browser.post('http://localhost:8000/v1/pet', json=pet_data, headers=hed)
        self.assertEqual(201, resp.status_code) 

        # than he tries to see the list of all pets
        resp = self.browser.get ('http://localhost:8000/v1/pet', headers=hed)

        self.assertEqual(200, resp.status_code) 
        self.assertEqual(pet_data["pet_name"] , resp.json()[0]["pet_name"])

        # than he update the pet name
        pet_data = {"pet_name":"fluffy dog","checked_in": False, "room": "string","deleted": False, "owner": "string"}
        resp = self.browser.put('http://localhost:8000/v1/pet/fluffy', json=pet_data, headers=hed)
        self.assertEqual(200, resp.status_code) 
        self.assertEqual({"status":"successfully updated "}, resp.json())

if __name__ == '__main__':  
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()