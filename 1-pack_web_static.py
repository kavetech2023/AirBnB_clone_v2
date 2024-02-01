#!/usr/bin/python3
"""Defines a function do_pack() which generates a .tgz archive
from the contents of the web_static folder"""

from fabric.api import *
from datetime import datetime
import os

def do_pack():
    """Generate an archive of /web_static folder"""
    try:
        os.makedirs("versions", exist_ok=True)
        date = datetime.now().strftime('%Y%m%d%H%M%S')
        fn = "versions/web_static_{}.tgz".format(date)

        # Use capture=True to capture the output of the command
        out = local("tar -czvf {} ./web_static/".format(fn), capture=True)

        # Check the return code of the command (0 means success)
        if out.return_code == 0:
            return fn
        else:
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
