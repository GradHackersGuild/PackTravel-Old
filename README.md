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
<a href="https://github.com/Prachit99/PackTravel/blob/main/images/video1155969440.mp4" target="_blank">Link to Video 2</a>


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
  <li>Google map route display</li>
  <li>Search and view other rides</li>
  <li>Join a PackTravel Ride</li>
  <li>Check all your rides</li>
  <li>See status of your requested rides</li> 
  <li>Approve who can ride with you</li>
  <li> Delete a Ride</li>
  
</ul>


<h2> Who can use our app?</h2>

  1. If you are a user who is visiting our app, you can sign up as a user with view access to rides. You can edit or create your own ride.
  2. If you are an admin user, you can create, view, update and delete rides and schedule rides.
  3. To request for admin privileges, please email on help@packtravel.io with the purpose of use. 

  - ### Prerequisite:
      - Download [Python3.x](https://www.python.org/downloads/release/python-380/).
      - Download [Django](https://docs.djangoproject.com/en/4.1/topics/install/).

   ## Run Locally

Create a virtual environment:

```bash
  python3.8 -m venv env
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
  git clone https://github.com/GradHackersGuild/PackTravel-Old
```

Go to the project directory

```bash
  cd PackTravel
```

Install dependencies

```bash 
  pip install -r requirements.txt
```

Create API Keys
1) Go to [google api keys](https://developers.google.com/maps/documentation/embed/get-api-key) and create API of your own. 
2) Then replace every instance of 'your_google_api_key' with the key you created in the entire codebase. 

Create MongoDB User to Connect to a dB 
1) Go to [mongodb atlas](https://cloud.mongodb.com/)
2) Create a new database or visit existing one.
3) Create new cluster called pack-travel.
4) Click on connect -> mongodB for VS Code.
5) This will give you one endpoint like below.

![image](https://github.com/user-attachments/assets/b39e2ba4-26e8-4071-a989-f62e0acb42f6)

1) Go to Database Access.
2) Create new user.
3) Enter username and password.
4) Put the password in config.ini file
5) Replace the current endpoint in utils.py that you with the newly created endpoint
6) Populate the username
7) Password has already been taken care of in the step 4 
 

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



## Discord Channel
<a href="https://discord.com/channels/1290739583042191420/1290739583042191423"><img src="https://github.com/user-attachments/assets/aff2b82a-677c-43da-be9e-73fcda385960" width="100px" height="100px"/></a>



## Contributors 

<table>
  <tr>
    <td align="center"><a href="https://github.com/MakarandPundlik"><img src="https://avatars.githubusercontent.com/u/65530539?v=4" width="100px;" alt=""/><br /><sub><b>Makarand Pundlik</b></sub></a></td>
    <td align="center"><a href="https://github.com/V4run14"><img src="https://avatars.githubusercontent.com/u/59575040?v=4" width="100px;" alt=""/><br /><sub><b>Varun Varatharajan</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/michellevarghese"><img src="https://avatars.githubusercontent.com/u/73420769?v=4" width="100px;" alt=""/><br /><sub><b>Michelle Varghese</b></sub></a><br /></td>
  </tr>
</table>


