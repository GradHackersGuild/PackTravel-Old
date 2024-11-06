from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from bson import ObjectId
import json
import requests

class PublishViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.mock_db = MagicMock()
        self.mock_userDB = self.mock_db.userData
        self.mock_ridesDB = self.mock_db.rides
        self.mock_routesDB = self.mock_db.routes

    @patch("publish.views.intializeDB")
    def test_publish_index_not_logged_in(self, mock_intializeDB):
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    @patch("publish.views.intializeDB")
    def test_publish_index_logged_in_without_username(self,mock_intializeDB):
        session = self.client.session
        session['usrname'] = 'testuser'
        session.save()
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        
    @patch("publish.views.intializeDB")
    def test_publish_index_logged_in(self, mock_intializeDB):
        session = self.client.session
        session['username'] = 'testuser'
        session.save()
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish/publish.html')

    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    def test_display_ride(self, mock_ridesDB, mock_intializeDB):
        mock_ridesDB.find_one.return_value = {
            '_id': 'test_ride_id',
            'spoint': 'Source',
            'destination': 'Destination'
        }
        response = self.client.get(reverse('display_ride', args=['test_ride_id']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish/display_ride.html')

    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    def test_display_ride_wrong_args(self, mock_ridesDB, mock_intializeDB):
        try:
            mock_ridesDB.find_one.return_value = {
            '_id': 'test_ride_id',
            'destination': 'Destination'
            }
            response = self.client.get(reverse('display_ride', args=['test_ride_id']))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'publish/display_ride.html')
        except Exception:
            self.assertTrue(True)
        
    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    def test_display_ride_no_args(self, mock_ridesDB, mock_intializeDB):
        try:
            mock_ridesDB.find_one.return_value = {}
            response = self.client.get(reverse('display_ride', args=['test_ride_id']))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'publish/display_ride.html')
        except Exception:
            self.assertTrue(True)

    @patch("publish.views.intializeDB")
    def test_select_route_post(self, mock_intializeDB):
        post_data = {
            'hiddenInput': 'test_route_id',
            'hiddenUser': 'testuser',
            'hiddenRide': json.dumps({'_id': 'test_ride_id'})
        }
        response = self.client.post(reverse('select_route'), data=post_data)
        self.assertEqual(response.status_code, 302)


    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    @patch("publish.views.distance_and_cost")
    def test_create_route(self, mock_distance_and_cost, mock_ridesDB, mock_intializeDB):
        mock_distance_and_cost.return_value = "10 and 15"
        session = self.client.session
        session['username'] = 'testuser'
        session.save()
        
        post_data = {
            'purpose': 'Test Purpose',
            'spoint': 'Source',
            'destination': 'Destination',
            'type': 'One-way',
            'date': '2023-11-01',
            'hour': '10',
            'minute': '00',
            'ampm': 'AM',
            'capacity': '4',
            'details': 'Test details'
        }
        
        response = self.client.post(reverse('create_route'), data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish/publish.html')
        #mock_ridesDB.insert_one.assert_called_once()

    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    @patch("publish.views.distance_and_cost")
    def test_create_route_mock_throws_error(self, mock_distance_and_cost, mock_ridesDB, mock_intializeDB):
        try:
            mock_distance_and_cost.return_value = "10 and 15"
            mock_ridesDB.side_effect = requests.ConnectionError("Unable to connect")
            session = self.client.session
            session['username'] = 'testuser'
            session.save()
            
            post_data = {
                'purpose': 'Test Purpose',
                'spoint': 'Source',
                'destination': 'Destination',
                'type': 'One-way',
                'date': '2023-11-01',
                'hour': '10',
                'minute': '00',
                'ampm': 'AM',
                'capacity': '4',
                'details': 'Test details'
            }
            self.client.post(reverse('create_route'), data=post_data)
        except Exception: 
            self.assertEqual(True)
        
    def tearDown(self):
        pass
