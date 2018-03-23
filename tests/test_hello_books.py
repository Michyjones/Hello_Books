import unittest


class UserAuthentication(unittest.TestCase):
    def setUp(self):
        """Initialises the tests"""
        self.client = run.app.test_client()
        db.create_all()
        user = {"email": "michyjones@gmail.com", "password": "qwerty123"}
        data = json.dumps(user)
        self.client.post(
            "/v1/auth/register", data=data,
            content_type="application/json")

        response = self.client.post(
            "/v1/auth/login", data=userdata, content_type="application/json")
        self.token = json.loads(response.data.decode())['Authorization']

    def test_register_user(self):
        """test if a user is created successfully """
        user = {"email": "michyjones@gmail.com",
                "password": "qwerty123", "role": "user"}
        data = json.dumps(user)
        response = self.client.post(
            "/v1/auth/register", data=data,
            content_type="application/json")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data)
        self.assertEqual(output['message'], "User created successfully")

    def test_register_user_cannot_use_empty_credentials(self):
        user = {"email": " ", "password": " ", "role": " "}
        data = json.dumps(user)
        response = self.client.post(
            "/v1/auth/register", data=data,
            content_type="application/json")
        self.assertEqual(response.status_code, 401)
        output = json.loads(response.data)
        self.assertEqual(output['message'], "Invalid username/password")

    def test_register_user_already_exists(self):
        user = {"email": "michyjones@gmail.com", "password": "qwerty123"}
        data = json.dumps(user)
        response = self.client.post(
            "/v1/auth/register", data=data,
            content_type='application/json')
        self.assertEqual(response.status_code, 409)
        output = json.loads(response.data.decode())
        self.assertEqual(output['error'], "User already exist")

    def test_register_user_role_is_admin(self):
          """test if a user is created successfully """
        user = {"email": "michyjones@gmail.com", "password": 
        "qwerty123" "role" :"admin"}
        data = json.dumps(user)
        response = self.client.post(
            "/v1/auth/register", data=data,
            content_type="application/json")
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data)
        self.assertEqual(output['message'], "Admin created successfully")
        pass

    def test_login_user(self):
          """Test user can login """
        user = {"email": "michyjones@gmail.com", "password": "qwerty123"}
        data = json.dumps(user)
        response = self.client.post(
            "/v1/auth/login", data=data, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        output = json.loads(response.data.decode())
        self.assertEqual(output['message'],
                         "You have logged in successfully")

    def test_login_user_invlaid_creadentials(self):

    """Test a user cannot login in with invalid credentials"""
        user = user = {"email": "michael@gmail.com", "password": "qwerty123"}
        data = json.dumps(user)
        response = self.client.post(
            "/v1/auth/login", data=data, content_type='application/json')
        self.assertEqual(response.status_code, 401)
        output = json.loads(response.data.decode())
        self.assertEqual(output['error'], "Invalid username/password")


class User_book(unittest.TestCase):
    """docstring for User_book"""

    def test_admin_can_add_book(self)
        pass

    def test_admin_can_delete_book(self):

        pass

    def test_admin_can_update_book(self):

        pass

     def tearDown(Self):
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
