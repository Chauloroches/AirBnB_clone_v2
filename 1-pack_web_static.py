#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os
# Fabric script that generates a .tgz archive from the contents of the web_static folder of your AirBnB

def do_pack():
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")
    
        now = datetime.now()
        archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))
    
        local("tar -cvzf {} web_static".format(archive_name))
        
        if os.path.exists(archive_name):
            return archive_name
        else:
            return None
    except:
        return None

