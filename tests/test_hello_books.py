import unittest


class UserAuthentication(unittest.TestCase):
 def setUp(self):
        """Initialises the tests"""
        self.client = run.app.test_client()
        db.create_all()
        user = {"username": "rozzah", "password": "password"}
        userdata = json.dumps(user)
        self.client.post(
            "/v1/auth/register", data=userdata,
            content_type="application/json")

        response = self.client.post(
            "/v1/auth/login", data=userdata, content_type="application/json")
        self.token = json.loads(response.data.decode())['Authorization']








    def test_register_user(self):
        pass

    def test_register_user_cannot_use_empty_credentials(self):

        pass

    def test_register_user_already_exists(self):

        pass

    def test_register_user_role_is_admin_or_user(self):
        pass

    def test_login_user(self):
        pass

    def test_login_user_invlaid_creadentials(self):

        pass


class User_book(unittest.TestCase):
    """docstring for User_book"""

    def test_admin_can_add_book(self)
        pass

    def test_admin_can_delete_book(self):

        pass

    def test_admin_can_update_book(self):

        pass


if __name__ == '__main__':
    unittest.main()