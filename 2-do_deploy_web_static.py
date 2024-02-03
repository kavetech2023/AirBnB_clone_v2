#!/usr/bin/python3
from fabric.api import *
from os.path import exists

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
    run("mv {}/web_static/* {}".format(release_path, release_path))
    # Delete the link /data/web_static/current from the web server
    run("rm -rf {}/web_static".format(release_path))
    # Delete the link /data/web_static/current from the web server
    run("rm -rf {}".format(current_path))
    # Create a new the symbolic link /data/web_static/current on the web server
    run("ln -s {} {}".format(release_path, current_path))
    return True
