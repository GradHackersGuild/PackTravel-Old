from django.test import TestCase, Client
from django.urls import reverse
from unittest.mock import patch, MagicMock
from bson import ObjectId
import json
import uuid

class PublishViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.mock_db = MagicMock()
        self.mock_userDB = self.mock_db.userData
        self.mock_ridesDB = self.mock_db.rides
        self.mock_routesDB = self.mock_db.routes

    @patch("publish.views.intializeDB")
    def test_publish_index_not_logged_in(self):
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    @patch("publish.views.intializeDB")
    def test_publish_index_logged_in(self):
        session = self.client.session
        session['usrname'] = 'testuser'
        session.save()
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))
        
    @patch("publish.views.intializeDB")
    def test_publish_index_logged_in(self):
        session = self.client.session
        session['username'] = 'testuser'
        session.save()
        response = self.client.get(reverse('publish'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish/publish.html')

    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    def test_display_ride(self, mock_ridesDB):
        mock_ridesDB.find_one.return_value = {
            '_id': 'test_ride_id',
            'spoint': 'Source',
            'destination': 'Destination'
        }
        response = self.client.get(reverse('display_ride', args=['test_ride_id']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'publish/display_ride.html')

    @patch("publish.views.intializeDB")
    def test_select_route_post(self):
        post_data = {
            'hiddenInput': 'test_route_id',
            'hiddenUser': 'testuser',
            'hiddenRide': json.dumps({'_id': 'test_ride_id'})
        }
        response = self.client.post(reverse('select_route'), data=post_data)
        self.assertEqual(response.status_code, 302)
        
    @patch("publish.views.intializeDB")
    def test_select_route_post(self):
        post_data = {
            '_id': 'test_ride_id',
            'destination': 'Destination'
        }
        response = self.client.post(reverse('select_route'), data=post_data)
        self.assertEqual(response.status_code, 302)

    @patch("publish.views.intializeDB")
    @patch("publish.views.ridesDB")
    @patch("publish.views.distance_and_cost")
    def test_create_route(self, mock_distance_and_cost):
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

    def tearDown(self):
        pass
