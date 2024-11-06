from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from bson import ObjectId


class SearchViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.mock_db = MagicMock()
        self.mock_userDB = self.mock_db.userData
        self.mock_ridesDB = self.mock_db.rides

    @patch("search.views.intializeDB")
    @patch("search.views.ridesDB")
    def test_search_index_not_logged_in(self, mock_ridesDB, mock_intializeDB):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    @patch("search.views.intializeDB")
    @patch("search.views.ridesDB")
    def test_search_index_logged_in(self, mock_ridesDB, mock_intializeDB):
        session = self.client.session
        session['username'] = 'testuser'
        session.save()

        mock_ridesDB.find.return_value = [
            {
                '_id': 'ride1',
                'owner': 'otheruser',
                'availability': 2,
                'requested_users': [],
                'confirmed_users': []
            },
            {
                '_id': 'ride2',
                'owner': 'testuser',
                'availability': 1,
                'requested_users': [],
                'confirmed_users': []
            }
        ]

        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')
        self.assertContains(response, 'ride1')

    @patch("search.views.intializeDB")
    @patch("search.views.ridesDB")
    def test_search_index_user_in_requested_users(self, mock_ridesDB, mock_intializeDB):
        session = self.client.session
        session['username'] = 'testuser'
        session.save()

        mock_ridesDB.find.return_value = [
            {
                '_id': 'ride1',
                'owner': 'otheruser',
                'availability': 2,
                'requested_users': ['testuser'],
                'confirmed_users': []
            }
        ]

        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')

    @patch("search.views.intializeDB")
    @patch("search.views.ridesDB")
    def test_search_index_user_in_confirmed_users(self, mock_ridesDB, mock_intializeDB):
        session = self.client.session
        session['username'] = 'testuser'
        session.save()

        mock_ridesDB.find.return_value = [
            {
                '_id': 'ride1',
                'owner': 'otheruser',
                'availability': 2,
                'requested_users': [],
                'confirmed_users': ['testuser']
            }
        ]

        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search/search.html')

    @patch("search.views.intializeDB")
    @patch("search.views.ridesDB")
    def test_join_ride_not_logged_in(self, mock_ridesDB, mock_intializeDB):
        response = self.client.get(reverse('join_ride', args=['ride1']))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    @patch("search.views.intializeDB")
    @patch("search.views.ridesDB")
    def test_join_ride_logged_in(self, mock_ridesDB, mock_intializeDB):
        session = self.client.session
        session['username'] = 'testuser'
        session.save()

        mock_ridesDB.update_one.return_value = None

        response = self.client.get(reverse('join_ride', args=['ride1']))
        self.assertEqual(response.status_code, 200)
        mock_ridesDB.update_one.assert_called_once_with(
            {"_id": "ride1"},
            {"$push": {"requested_users": "testuser"}}
        )

    def test_is_user_in_list(self):
        from search.views import is_user_in_list

        self.assertTrue(is_user_in_list('user1', ['user1', 'user2', 'user3']))
        self.assertFalse(is_user_in_list('user4', ['user1', 'user2', 'user3']))
        self.assertFalse(is_user_in_list('user1', []))
        self.assertFalse(is_user_in_list('', ['user1', 'user2', 'user3']))
        self.assertFalse(is_user_in_list(None, ['user1', 'user2', 'user3']))

    def tearDown(self):
        pass
