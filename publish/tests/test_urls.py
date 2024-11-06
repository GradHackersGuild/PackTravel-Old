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

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from publish.views import publish_index, display_ride,create_route,select_route


class TestUrl(SimpleTestCase):

    def test_publish_index_resolved(self):
        url = reverse('publish')
        self.assertEquals(resolve(url).func, publish_index)

    def test_create_ride_resolved(self):
        url = reverse('create_route')
        self.assertEquals(resolve(url).func, create_route)

    def test_login_resolved(self):
        url = reverse('select_route')
        self.assertEquals(resolve(url).func, select_route)

    # def test_add_route_resolved(self):
    #     url = reverse('add_route')
    #     self.assertEquals(resolve(url).func, add_)

