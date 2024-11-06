import os
import sys
def myfunc():
    with open(os.path.join(sys.path[0], "config.ini"), "r") as f:
        content = f.readlines()
        print(content)
    

myfunc()