import os
import sys
import certifi
from pymongo import MongoClient


def get_client():
    #with open(os.path.join(sys.path[0], "config.ini"), "r") as f:
        #content = f.readlines()
    content="Varun1406"    
    client = MongoClient(
        "mongodb+srv://vvarath:" + content + "@cluster0.wc05z.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=certifi.where())
        #"mongodb+srv://Aoishi:" + content[0] + "@cluster0.zpuftvw.mongodb.net/?retryWrites=true&w=majority",

    return client
