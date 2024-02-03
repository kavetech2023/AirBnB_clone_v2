#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os
from os.path import exists


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


"""a Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""


env.hosts = ['100.25.3.52', '35.153.226.125']


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    # Check if the archive path exists
    if not exists(archive_path):
        return False
    # Get the archive filename without extension
    archive_file = archive_path.split('/')[-1]
    archive_name = archive_file.split('.')[0]
    # Define the remote paths
    tmp_path = "/tmp/{}".format(archive_file)
    release_path = "/data/web_static/releases/{}".format(archive_name)
    current_path = "/data/web_static/current"
    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, tmp_path)
    # Uncompress the archive to the /data/web_static/releases/
    run("mkdir -p {}".format(release_path))
    run("tar -xzf {} -C {}".format(tmp_path, release_path))
    # Delete the archive from the web server
    run("rm {}".format(tmp_path))
    # Delete the symbolic link /data/web_static/current from the web server
    run("mv {}/web_static/* {}".format(release_p
