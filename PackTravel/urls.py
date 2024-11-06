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

"""PackTravel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from user import views as userView
from search import views as searchViews
from publish import views as publishViews
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', searchViews.search_index, name = 'search'),
    path('publish/', publishViews.publish_index, name = 'publish'),
    path('index/', userView.index, name ='index'),
    path('', userView.index, name ='index'),
    path('index/<username>',userView.index, name='index'),
    path('register/', userView.register, name='register'),
    path('logout/', userView.logout, name='logout'),
    path('login/', userView.login, name='login'),
    path('create_route/', publishViews.create_route, name='create_route'),
    # path('add_route/', publishViews.add_route, name='add_route'),
    path('select_route/', publishViews.select_route, name='select_route'),
    path('display_ride/<ride_id>', publishViews.display_ride, name='display_ride'),
    path('accounts/', include('allauth.urls')),
    path('logout/', LogoutView.as_view()),
    path('myrides/', userView.my_rides, name = 'my_rides'),
    path('delete_ride/<ride_id>', userView.delete_ride, name = 'delete_ride'),
    path('join_ride/<ride_id>',searchViews.join_ride,name='join_ride'),
    path('approve_rides/<ride_id>',userView.approve_rides,name='approve_rides'),
    path('approve_user/<ride_id>/<user_id>',userView.approve_user,name='approve_user'),
    path('ride_status/',userView.requested_rides,name='requested_rides')
]
