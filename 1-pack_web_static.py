#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

"""Fabric script that generates a .tgz archive from
the contents of the web_static folder"""


def do_pack():
    """Create a tar gzipped archive of the web_static folder"""
    # Create the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    # Generate the archive name based on the current date and time
    now = datetime.now()
    archive_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                        now.month,
                                                        now.day,
                                                        now.hour,
                                                        now.minute,
                                                        now.second)
    # Create the archive using the tar command
    archive_path = "versions/{}".format(archive_name)
    result = local("tar -cvzf {} web_static".format(archive_path))
    # Return the archive path if successful, otherwise None
    if result.succeeded:
        return archive_path
    else:
        return None
