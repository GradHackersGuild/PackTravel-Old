
"""
MIT License

Copyright (c) 2022 Makarand Pundlik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from django.test import TestCase, Client, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.urls import reverse
from unittest.mock import patch, MagicMock
from bson import ObjectId
import hashlib
from user.views import add_user_to_session

class UserViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.mock_db = MagicMock()
        self.mock_userDB = self.mock_db.userData
        self.mock_ridesDB = self.mock_db.rides
        self.factory = RequestFactory()
        self.user_data = {
            "username": "testuser",
            "unityid": "u123456",
            "fname": "Test",
            "lname": "User",
            "email": "testuser@example.com",
            "phone": "1234567890"
        }

    @patch("user.views.intializeDB")
    @patch("user.views.userDB")
    def test_register_unique_username(self, mock_userDB, mock_intializeDB):
        mock_userDB.find_one.return_value = None  # Simulate username is unique

        form_data = {
            "username": "testuser",
            "unityid": "testunityid",
            "first_name": "Test",
            "last_name": "User",
            "email": "test@example.com",
            "password1": "password123",
            "phone_number": "1234567890"
        }
        response = self.client.post(reverse("register"), data=form_data)
        self.assertEqual(response.status_code, 302)
        #self.assertRedirects(response, reverse("index", kwargs={"username": self.username}))

    @patch('user.views.intializeDB')
    @patch('user.views.userDB')
    def test_login_user(self, mock_userDB, mock_initializeDB):
        mock_userDB.return_value = self.mock_userDB
        login_data = {
            "username": "testuser",
            "password": "password123"
        }
        hashed_password = hashlib.sha256(login_data["password"].encode()).hexdigest()
        self.mock_userDB.find_one.return_value = {
            "username": "testuser",
            "password": hashed_password,
            "unityid": "u123456",
            "fname": "Test",
            "lname": "User",
            "email": "testuser@example.com",
            "phone": "1234567890"
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertEqual(response.status_code, 200)  # Redirecting to login after login gives 200
        
    @patch('user.views.intializeDB')
    @patch('user.views.userDB')
    def test_login_wrong_password(self, mock_userDB, mock_initializeDB):
        mock_userDB.return_value = self.mock_userDB
        login_data = {
            "username": "testuser",
            "password": "wrongpassword"
        }
        hashed_password = hashlib.sha256("password123".encode()).hexdigest()
        self.mock_userDB.find_one.return_value = {
            "username": "testuser",
            "password": hashed_password,
            "unityid": "u123456",
            "fname": "Test",
            "lname": "User",
            "email": "testuser@example.com",
            "phone": "1234567890"
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertTemplateUsed(response, "user/login.html")
        self.assertIn("alert", response.context)
        self.assertEqual(response.context["alert"], "Incorrect username or password.")
        
    @patch('user.views.intializeDB')
    @patch('user.views.userDB')
    def test_login_wrong_user(self, mock_userDB, mock_initializeDB):
        mock_userDB.return_value = self.mock_userDB
        login_data = {
            "username": "wrongtestuser",
            "password": "password123"
        }
        hashed_password = hashlib.sha256(login_data["password"].encode()).hexdigest()
        self.mock_userDB.find_one.return_value = {
            "username": "testuser",
            "password": hashed_password,
            "unityid": "u123456",
            "fname": "Test",
            "lname": "User",
            "email": "testuser@example.com",
            "phone": "1234567890"
        }
        response = self.client.post(reverse('login'), data=login_data)
        self.assertTemplateUsed(response, "user/login.html")
        self.assertIn("alert", response.context)
        self.assertEqual(response.context["alert"], "Incorrect username or password.")

    def test_logout_user(self):
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn("username", self.client.session)

    @patch('user.views.intializeDB')
    @patch('user.views.ridesDB')
    def test_my_rides(self, mock_ridesDB, mock_initializeDB):
        mock_ridesDB.return_value = self.mock_ridesDB
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        self.mock_ridesDB.find.return_value = [{"_id": ObjectId(), "owner": "testuser", "destination": "City B"}]
        response = self.client.get(reverse('my_rides'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "testuser")

    @patch('user.views.intializeDB')
    @patch('user.views.ridesDB')
    @patch('user.views.userDB')
    def test_delete_ride(self, mock_userDB, mock_ridesDB, mock_initializeDB):
        mock_userDB.return_value = self.mock_userDB
        mock_ridesDB.return_value = self.mock_ridesDB
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        self.mock_userDB.find_one.return_value = {"username": "testuser"}
        self.mock_ridesDB.find_one.return_value = {"_id": ObjectId(), "owner": "testuser"}
        response = self.client.post(reverse('delete_ride', args=[str(ObjectId())]))
        self.assertEqual(response.status_code, 302)
        #self.mock_ridesDB.delete_one.assert_called_once()

    @patch('user.views.intializeDB')
    @patch('user.views.ridesDB')
    def test_requested_rides(self, mock_ridesDB, mock_initializeDB):
        mock_ridesDB.return_value = self.mock_ridesDB
        session = self.client.session
        session["username"] = "testuser"
        session.save()
        self.mock_ridesDB.aggregate.return_value = [
            {"_id": ObjectId(), "found_in_requested": True, "requested_users": ["testuser"]},
            {"_id": ObjectId(), "found_in_confirmed": True, "confirmed_users": ["testuser"]}
        ]
        response = self.client.get(reverse('requested_rides'))
        self.assertEqual(response.status_code, 200)

    @patch('user.views.ridesDB')
    def test_redirect_when_not_logged_in(self, mock_ridesDB):
        ride_id = "ride123"
        response = self.client.get(reverse("approve_rides", args=[ride_id]))
        self.assertRedirects(response, reverse("index"))
        self.assertEqual(self.client.session["alert"], "Please login to approve rides.")
    
    def _add_session_to_request(self, request):
        """Helper function to add session to the request object."""
        middleware = SessionMiddleware(lambda req: None) 
        middleware.process_request(request)
        request.session.save()

    def test_add_user_to_session(self):
        request = self.factory.get('/dummy-url')
        self._add_session_to_request(request)
        add_user_to_session(request, self.user_data)

        self.assertEqual(request.session['username'], self.user_data["username"])
        self.assertEqual(request.session['unityid'], self.user_data["unityid"])
        self.assertEqual(request.session['fname'], self.user_data["fname"])
        self.assertEqual(request.session['lname'], self.user_data["lname"])
        self.assertEqual(request.session['email'], self.user_data["email"])
        self.assertEqual(request.session['phone'], self.user_data["phone"])

    def test_missing_user_data_key(self):
        incomplete_user_data = {
            "username": "testuser",
            "unityid": "u123456",
            "fname": "Test",
            # "lname" key is missing
            "email": "testuser@example.com",
            "phone": "1234567890"
        }

        request = self.factory.get('/dummy-url')
        self._add_session_to_request(request)
        with self.assertRaises(KeyError):
            add_user_to_session(request, incomplete_user_data)
        
    #def tearDown(self):
    #    #Clear mocked data
    #    self.mock_userDB.delete_many.assert_called_with({})
    #    self.mock_ridesDB.delete_many.assert_called_with({})