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

from http.client import HTTPResponse
from django.shortcuts import render, redirect
from numpy import True_, dtype
import requests
import json
from cab_model.predict import predict_price
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from publish.forms import RideForm
from utils import get_client

import uuid
# from django.http import HttpResponse

# Create your views here.
client = None
db = None
userDB = None
ridesDB = None
routesDB = None


def intializeDB():
    """Initializes global MongoDB client and database collections for users, rides, and routes."""
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB = db.rides
    routesDB = db.routes


def publish_index(request):
    """Renders the publish page if the user is logged in; otherwise, redirects to the index with an alert."""
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    return render(request, 'publish/publish.html', {"username": request.session['username'], "alert": True})


def display_ride(request, ride_id):
    """Displays details of a specific ride based on ride_id by fetching data from the rides database."""    
    intializeDB()
    print("Ride id", ride_id)
    ride = ridesDB.find_one({'_id': ride_id})
    result = {
        "spoint": ride['spoint'],
        "destination": ride['destination']
    }
    return render(request, "publish/display_ride.html", {"ride_id": ride["_id"], "ride": ride})


def select_route(request):
    """Processes route selection from a POST request and redirects to the display ride page with the selected ride's details."""
    intializeDB()
    if request.method == 'POST':
        route_id = request.POST.get("hiddenInput")
        username = request.POST.get('hiddenUser')
        ride = request.POST.get('hiddenRide')
        print("route from form: ", route_id)
        ride = ride.replace("\'", "\"")
        ride = json.loads(ride)
        return redirect(display_ride, ride_id=ride['_id'])
    return render(request, 'publish/publish.html', {"username": username})


def routeSelect(username, routes):
    """Returns the first route ID that matches the user's rides or None if no match is found or input is invalid."""
    intializeDB()
    user = userDB.find_one({"username": username})
    if user == None or routes == None:
        print("returning NONE")
        return None

    user_routes = user['rides']
    print("User routes: ", user_routes)
    for route in routes:
        if route['_id'] in user_routes:
            print("FOUND")
            return route['_id']
    return None


def get_routes(ride):
    """Retrieves and returns a list of routes associated with a ride, or None if no route ID is found."""
    routes = []
    if 'route_id' not in ride:
        return None
    route_ids = ride['route_id']
    for route_id in route_ids:
        route = routesDB.find_one({'_id': route_id})
        if not route:
            pass
        # route['id'] = route.pop('_id')
        routes.append(route)
    return routes


def distance_and_cost(source, destination, date, hour, minute, ampm):
    """Method to retrieve distance between source and origin"""
    api_key = "your_google_api_key"
    date = date.split("-")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?" + \
        "origins=" + source + "&destinations=" + destination + "&key=" + api_key
    if ampm.lower() == "pm":
        hour = str(int(hour) + 12)
    date_time = f"{date[2]}-{date[1]}-{date[0]} {hour}:{minute}:{00}"
    response = requests.get(url, timeout=100)
    distance_data = response.json()
    distance_miles = distance_data["rows"][0]["elements"][0]["distance"]["value"]/1600
    p = predict_price(distance_miles, date_time)
    cost1, cost2 = p.generate_data_return_price()
    cost = cost1 + " and " + cost2
    return cost


def create_route(request):
    """Handles the creation of a new route based on the data received in the request."""
    if request.method == 'POST':
        intializeDB()
        ride = {
            "_id": str(uuid.uuid4()),
            "purpose": request.POST.get('purpose'),
            "spoint": request.POST.get('spoint'),
            "destination": request.POST.get('destination'),
            "type": request.POST.get('type'),
            "date": request.POST.get("date"),
            "hour": request.POST.get("hour"),
            "minute":  request.POST.get("minute"),
            "ampm": request.POST.get("ampm"),
            "availability": int(request.POST.get("capacity")),
            "max_size": int(request.POST.get("capacity")),
            "details": request.POST.get("details"),
            "owner": request.session["username"],
            "cost": distance_and_cost(request.POST.get("spoint"), request.POST.get("destination"), request.POST.get("date"), request.POST.get("hour"), request.POST.get("minute"), request.POST.get("ampm")),
            "requested_users": [],
            "confirmed_users": []
        }
        if ridesDB.find_one({"_id": ride["_id"]}) is None:
            ridesDB.insert_one(ride)
    return render(request, 'publish/publish.html', {"username": request.session['username']})

# Add Edit functionality

# Add Delete functionality
