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
from django.shortcuts import render,redirect
from numpy import True_, dtype
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
#from request import views as requestsViews
from publish.forms import RideForm
from utils import get_client

client = None
db = None
userDB = None
ridesDB  = None
routesDB  = None

def intializeDB():
    """Initializes global MongoDB client and database collections for users, rides, and routes."""
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB  = db.rides
    routesDB  = db.routes

def is_user_in_list(username,list):
    """Checks if a username is present in a given list and returns True if found, otherwise False."""
    try:
        list.index(username)
        return True
    except ValueError:
        return False
    
def search_index(request):
    """Searches for available rides and renders the search results page, allowing users to join if they meet criteria."""
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    processed = list(ridesDB.find())
    for ride in processed:
        ride['id'] = ride['_id']
        #if condition ensures, requestor is not already a part of requested users or approved users
        if request.session['username'] != ride['owner'] and ride['availability'] > 0 and not is_user_in_list(request.session['username'],ride['requested_users']) and not is_user_in_list(request.session['username'],ride['confirmed_users']):
            ride['allow_to_join'] = True
    return render(request, 'search/search.html', {"username": request.session['username'], "rides": processed})

def join_ride(request,ride_id):
    """Allows a logged-in user to join a ride by adding their username to the ride's requested users list."""
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    intializeDB()
    query = {"_id": ride_id}
    update = {"$push": {"requested_users": request.session['username']}}
    ridesDB.update_one(query,update)
    return search_index(request)