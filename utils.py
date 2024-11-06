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

import os
import sys
import certifi
from pymongo import MongoClient


def get_client():
    """Returns a MongoDB client connected to the specified Atlas cluster with secure TLS authentication."""
    with open(os.path.join(sys.path[0], "config.ini"), "r") as f:
        content = f.readlines()
        #file - config.ini stores password 
    client = MongoClient(
        "mongodb+srv://<username>:"+content[0]+"@cluster0.wc05z.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=certifi.where())
    return client
