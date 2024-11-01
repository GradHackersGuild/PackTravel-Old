from http.client import HTTPResponse
from django.shortcuts import render,redirect
from numpy import True_, dtype
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from request import views as requestsViews
from publish.forms import RideForm
from utils import get_client

client = None
db = None
userDB = None
ridesDB  = None
routesDB  = None

def intializeDB():
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB  = db.rides
    routesDB  = db.routes

def is_user_in_list(username,list):
    try:
        list.index(username)
        return True
    except ValueError:
        return False
    
def search_index(request):
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
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    intializeDB()
    query = {"_id": ride_id}
    update = {"$push": {"requested_users": request.session['username']}}
    ridesDB.update_one(query,update)
    return search_index(request)