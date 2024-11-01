from http.client import HTTPResponse
from django.shortcuts import render, redirect
import requests
import json
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from utils import get_client
from .forms import RegisterForm, LoginForm
import hashlib

client = None
db = None
userDB = None
ridesDB = None
routesDB = None


def intializeDB():
    global client, db, userDB, ridesDB, routesDB
    client = get_client()
    db = client.SEProject
    userDB = db.userData
    ridesDB = db.rides
    routesDB = db.routes


# Home page for PackTravel
def index(request, username=None):
    intializeDB()
    if request.user.is_authenticated:
        request.session["username"] = request.user.username
        request.session['fname'] = request.user.first_name
        request.session['lname'] = request.user.last_name
        request.session['email'] = request.user.email
        user = userDB.find_one({"username": request.user.username})
        if not user:
            userObj = {
                "username": request.user.username,
                "fname": request.user.first_name,
                "lname": request.user.last_name,
                "email": request.user.email,
                "rides": []
            }
            userDB.insert_one(userObj)
            print("User Added")
        else:
            print("User Already exists")
            print(f'Username: {user["username"]}')
        return render(request, 'home/home.html', {"username": request.session["username"]})
    if request.session.has_key('username'):
        return render(request, 'home/home.html', {"username": request.session["username"]})
    return render(request, 'home/home.html', {"username": None})


def add_user_to_session(request, userObj):
    request.session['username'] = userObj["username"]
    request.session['unityid'] = userObj["unityid"]
    request.session['fname'] = userObj["fname"]
    request.session['lname'] = userObj["lname"]
    request.session['email'] = userObj["email"]
    request.session['phone'] = userObj["phone"]


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data["password1"]
            intializeDB()
            # check whether username is unique
            if (userDB.find_one({"username": form.cleaned_data["username"]})):
                print('UserName Already Exists, please try different Username')
                return render(request, 'user/register.html', {"form": form})

            userObj = {
                "username": form.cleaned_data["username"],
                "unityid": form.cleaned_data["unityid"],
                "fname": form.cleaned_data["first_name"],
                "lname": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "password": hashlib.sha256(password.encode()).hexdigest(),
                "phone": form.cleaned_data["phone_number"]
            }
            userDB.insert_one(userObj)
            add_user_to_session(request=request, userObj=userObj)
            return redirect(index, username=request.session["username"])
        else:
            print(form.errors.as_data())
    else:
        if request.session.has_key('username'):
            return index(request, request.session['username'])
        form = RegisterForm()
    return render(request, 'user/register.html', {"form": form})


def logout(request):
    try:
        request.session.clear()
    except:
        pass
    return redirect(index)


# @describe: Existing user login
def login(request):
    intializeDB()
    if request.session.has_key('username'):
        return redirect(index, {"username": request.session['username']})
    else:
        if request.method == "POST":
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                passw = form.cleaned_data["password"]
                user = userDB.find_one({"username": username})

                if user and user["password"] == hashlib.sha256(form.cleaned_data["password"].encode()).hexdigest():
                    request.session["username"] = username
                    request.session['unityid'] = user["unityid"]
                    request.session['fname'] = user["fname"]
                    request.session['lname'] = user["lname"]
                    request.session['email'] = user["email"]
                    request.session["phone"] = user["phone"]
                    return redirect(index, request.session['username'])

        form = LoginForm()
        return render(request, 'user/login.html', {"form": form})


def my_rides(request):
    intializeDB()
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    processed = list(ridesDB.find({"owner": request.session["username"]}))
    rides = []
    for iter in processed:
        iter['id'] = iter['_id']
        rides.append(iter)
    return render(request, 'user/myride.html', {"username": request.session['username'], "rides": rides})


def delete_ride(request, ride_id):
    intializeDB()
    print(ride_id)
    user = userDB.find_one({"username": request.session['username']})
    ride = ridesDB.find_one({"_id": ride_id})

    # only owner can delete ride
    if ride is not None and ride["owner"] == request.session["username"]:
        ridesDB.delete_one({"_id": ride_id})
    return redirect("/ride_status")


def approve_rides(request, ride_id):
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to approve rides."
        return redirect('index')
    intializeDB()
    ride = ridesDB.find_one({"_id": ride_id})
    return render(request, "user/approve_rides.html", {"username": request.session['username'], "space": ride['availability'], "requested_users": ride['requested_users'], "approved_users": ride['confirmed_users'], "ride_id": ride_id})


def approve_user(request, ride_id, user_id):
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to approve rides."
        return redirect('index')
    intializeDB()
    ride = ridesDB.find_one({"_id": ride_id})
    ride['requested_users'].remove(user_id)
    ride['confirmed_users'].append(user_id)
    ride['availability'] -= 1
    ridesDB.replace_one({"_id": ride_id}, ride)
    return redirect("/ride_status")


def requested_rides(request):
    if not request.session.has_key('username'):
        request.session['alert'] = "Please login to create a ride."
        return redirect('index')
    intializeDB()
    username = request.session["username"]
    pipeline = [
        {
            "$match": {
                "$or": [
                    {"requested_users": username},
                    {"confirmed_users": username}
                ]
            }
        },
        {
            "$project": {
                "_id": 1,
                "purpose": 1,
                "spoint": 1,
                "destination": 1,
                "requested_users": 1,
                "confirmed_users": 1,
                "date": 1,
                "hour": 1,
                "minute": 1,
                "ampm": 1,
                "availability": 1,
                "max_size": 1,
                "found_in_requested": {
                    "$cond": {
                        "if": {"$in": [username, "$requested_users"]},
                        "then": True,
                        "else": False
                    }
                },
                "found_in_confirmed": {
                    "$cond": {
                        "if": {"$in": [username, "$confirmed_users"]},
                        "then": True,
                        "else": False
                    }
                }
            }
        }
    ]
    pipeline2 = [
        {
            "$match": {
                "owner": username,  # Filter by the rides owned by the user
                # Only get rides with pending requests
                "requested_users": {"$exists": True, "$not": {"$size": 0}}
            }
        },
        {
            "$project": {
                "_id": 1,
                "id": "$_id",
                "purpose": 1,
                "spoint": 1,
                "destination": 1,
                "requested_users": 1,
                "date": 1,
                "hour": 1,
                "minute": 1,
                "ampm": 1,
                "availability": 1,
                "max_size": 1  # Only return the requested users
            }
        }
    ]

    pipeline3 = [
        {
            "$match": {
                "$or": [
                    {"owner": username},
                    {"confirmed_users": username}
                ]
            }
        },
        {
            "$project": {
                "_id": 1,
                "id": "$_id",
                "spoint": 1,
                "destination": 1,
                "ride_type": 1,
                "date": 1,
                "hour": 1,
                "minute": 1,
                "availability": 1,
                "max_size": 1,
                "ampm": 1,
                "owner": 1,
                "confirmed_users": 1
            }
        }
    ]
    received_requests = list(ridesDB.aggregate(pipeline2))
    user_rides = list(ridesDB.aggregate(pipeline3))

    results = list(ridesDB.aggregate(pipeline))
    requested = [doc for doc in results if doc['found_in_requested']]
    confirmed = [doc for doc in results if doc['found_in_confirmed']]
    print(user_rides)

    return render(request, 'user/ride_status.html', {"username": request.session["username"], "requested": requested, "confirmed": confirmed, "received_requests": received_requests, "user_rides": user_rides})
