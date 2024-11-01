<div align="center">

<img style="width: 120px; height: 120px;" src="./images/wolf2.svg"></img>
# `PackTravel`



[![DOI](https://zenodo.org/badge/879310431.svg)](https://doi.org/10.5281/zenodo.14020210)
![Tests](https://github.com/GradHackersGuild/PackTravel-Old/actions/workflows/run_test_cases.yml/badge.svg)
[![Codecov](https://codecov.io/gh/GradHackersGuild/PackTravel-Old/branch/main_new/graph/badge.svg)](https://codecov.io/gh/GradHackersGuild/PackTravel-Old)
![Python Style Checker](https://github.com/GradHackersGuild/PackTravel-Old/actions/workflows/python_style_checker.yml/badge.svg)
![Lint Python](https://github.com/GradHackersGuild/PackTravel-Old/actions/workflows/pylint.yml/badge.svg)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT) 
[![contributors](https://img.shields.io/github/contributors/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://github.com/GradHackersGuild/PackTravel-Old/graphs/contributors)
[![Total Lines](https://img.shields.io/tokei/lines/github/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://img.shields.io/tokei/lines/github/GradHackersGuild/PackTravel-Old)
[![Issues](https://img.shields.io/github/issues/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://github.com/GradHackersGuild/PackTravel-Old/issues)
[![Closed Issues](https://img.shields.io/github/issues-closed-raw/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://github.com/GradHackersGuild/PackTravel-Old/issues?q=is%3Aissue+is%3Aclosed)
[![Pull Requests](https://img.shields.io/github/issues-pr/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://github.com/GradHackersGuild/PackTravel-Old/pulls)
[![Commit Activity](https://img.shields.io/github/commit-activity/w/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://github.com/GradHackersGuild/PackTravel-Old/graphs/commit-activity)
[![Repo Size](https://img.shields.io/github/repo-size/GradHackersGuild/PackTravel-Old?style=for-the-badge)](https://github.com/GradHackersGuild/PackTravel-Old)



</div>

## Flaws in Phase 1

- Only basic sign-up/login option which used to break multiple times.
- One was able to create Rides as well as Routes which would create a lot of data redundancy and multiple rides and routes even for the same source to destination travel ultimately causing more confusion to users.
- No scope of deleting or cancelling a ride or route.
- No scope for the user to track his/her rides creating problems for the user track his/her rides and routes and plan accordingly.
- Application was running only on local servers. Not deployed so very less usability scope as well as very less server support.


https://user-images.githubusercontent.com/18501895/205809978-14a5c1c0-65a3-4171-b6f2-f30449325088.mp4

## Enhancement and Improvements in Phase 2:
-  Restructed the database and object structure to improve efficiency and avoid data redundancy. 
- Users can create or join routes which would create or map the rides automatically based on the source and destination avoiding duplicate data and data redundancy.
-  Added User based Rides Page which would help the user to track his rides and work on it accordingly. 
- Added Google SSO Sign in functionality to add options to signing up which also covers security loopholes.
- Added delete/cancel ride functionality so that if the user has cancelled his plan of going to a particular destination, he/she can cancel/delete the ride so that others are not dependent on the same creating efficient and easy usability for the users.
- Deployed and Hosted the application on AWS making the application more stable, globally acccessible and not dependent on any local machine.

<a href="https://github.com/Prachit99/PackTravel/blob/main/images/video1155969440.mp4" target="_blank">Link to Video 2</a>

<h2>Scalability</h2>

How can we scale this project? What are the shortcomings which can be covered if we scale it? Everything answered and explained in the in-detailed document attached below.

<a href="https://github.com/Prachit99/PackTravel/blob/36a6b9848f74c52ebe0ccedfef6c0846d98a230d/scalability.md" target="_blank">Click here to know about Scaling this project to the next level</a>


<h2>What is Packtravel?</h2>

Most of the university students do not have a car to travel off-campus and rely mostly on the Wolfline. But what if someone wants to travel outside Wolfline's limit? Well... why not collaborate on PackTravel to travel off-campus by a cab, rental car, etc.

**So, let's go for Packtravel**

https://user-images.githubusercontent.com/111834635/194171771-962a585e-5dc7-4ea3-af35-732ebd34e76c.mp4

**Built Using:**
</br>
<code><a href="https://www.python.org/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194173533-37cd4997-55f3-4bb1-87bd-1a16a3af53aa.png"></a></code>
<code><a href="https://www.djangoproject.com/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194172149-ff6a56be-3025-4d2c-8cdb-b9a7e3f87259.png"></a></code>
<code><a href="https://www.mongodb.com/" target="_blank"><img height="50" src="https://user-images.githubusercontent.com/111834635/194173280-628ecfc0-21ae-4870-8e22-711e6da83820.png"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Glossary/HTML5" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_html5/w3_html5-ar21.svg"></a></code>
<code><a href="https://developer.mozilla.org/en-US/docs/Web/CSS" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/w3_css/w3_css-ar21.svg"></a></code>
<code><a href="https://www.javascript.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/javascript/javascript-ar21.svg"></a></code>
<code><a href="https://getbootstrap.com/" target="_blank"><img height="50" src="https://www.vectorlogo.zone/logos/getbootstrap/getbootstrap-ar21.svg"></a></code>


<h2>Features</h2>

<ul>
  <li>Create a PackTravel Ride</li>
  <li>Create mmultiple routes to reach a ride's destination:  Bus, Cab or Personal</li>
  <li>Search and view other's rides</li>
  <li>Join a PackTravel Ride's route</li>
  <li>Check all your rides</li>
  <li>Modify your Ride</li>
  <li> Delete a Ride</li>
  
</ul>


<h2> Who can use our app?</h2>

  1. If you are a user who is visiting our app, you can sign up as a user with view access to rides. You can edit or create your own ride.
  2. If you are an admin user, you can create, view, update and delete rides and schedule rides.
  3. To request for admin privileges, please email on help@packtravel.io with the purpose of use. 

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/).
      - Download [Django](https://docs.djangoproject.com/en/4.1/topics/install/).

   ## Run Locally

Create a virtual environment:

```bash
  python3.x -m venv env
```

Activate the virtual environment:
Linux/MacOS:
```bash
  source env/bin/activate
```
Windows:
```bash
  ./env/Scripts/activate
```

Clone the project

```bash
  git clone https://github.com/Prachit99/PackTravel.git
```

Go to the project directory

```bash
  cd PackTravel
```

Install dependencies

```bash 
  pip install -r requirements.txt
```

Start the server

```bash
  python manage.py migrate
  python manage.py runserver
```



     - Site gets hosted at:
       `http://127.0.0.1:8000/`
       
## Tools
- [Preetier Code Formatter](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
- [JS-HTML-CSS Formatter](https://marketplace.visualstudio.com/items?itemName=lonefy.vscode-JS-CSS-HTML-formatter)
- [PyLint](https://pylint.org/)

## Functionalities in Action 

- **Sign Up Page**
<img src="/images/Register.gif" width="800" height="400"/>

- **Login Page**
<img src="/images/Login%20(1).gif" width="800" height="400"/>

- **Creating a Ride**
<img src="/images/Create1.gif" width="800" height="400"/>
<img src="/images/Create2.gif" width="800" height="400"/>

- **Adding New Route**
<img src="/images/AddRoute11.gif" width="800" height="400"/>
<img src="/images/AddRoute12.gif" width= "800" height="400"/>

- **Search for a Ride**
<img src="/images/Search.gif" width="800" height="400"/>

- **My Rides**

<img src="/images/myRides.gif" width="800" height="400"/>



## Chat Channel

<code><a href="https://seproject-bvz2267.slack.com/archives/C045KE3RW9L" target="_blank"><img height="50" width="100" src="https://user-images.githubusercontent.com/111834635/194175304-834d5663-b6bb-4e38-981d-98bc1bf028b8.png"></a></code>


## Contributors 

<table>
  <tr>
    <td align="center"><a href="https://github.com/Prachit99"><img src="https://avatars.githubusercontent.com/Prachit99" width="100px;" alt=""/><br /><sub><b>Prachit99</b></sub></a></td>
    <td align="center"><a href="https://github.com/Darkspur"><img src="https://avatars.githubusercontent.com/Darkspur" width="100px;" alt=""/><br /><sub><b>Sahil Sawant Joshi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/ashishjoshi2605"><img src="https://avatars.githubusercontent.com/ashishjoshi2605" width="100px;" alt=""/><br /><sub><b>Ashish Joshi</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/sankettangade"><img src="https://avatars.githubusercontent.com/sankettangade" width="100px;" alt=""/><br /><sub><b>Sanket Tangade</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/karan-47"><img src="https://avatars.githubusercontent.com/karan-47" width="100px;" alt=""/><br /><sub><b>Karan Gala</b></sub></a><br /></td>
  </tr>
</table>


