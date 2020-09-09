# install.py
# Version: 1.0.0
# Installs dependencies needed for FCW
# Author: Nazmus Nasir
# Website: https://www.easyprogramming.net

import os
from shutil import copy2


def install_dependencies():
    print("================== Start Installing PIP and venv ==================")
    os.system("sudo apt install python3-pip python3-venv -y")
    print("================== Completed Installing PIP ==================")

    print("================== Start Updating PIP ==================")
    os.system("sudo pip3 install --upgrade pip")
    print("================== Completed Updating PIP ==================")

    print("================== Start Installing Setuptools and Libatlas ==================")
    os.system("sudo apt install python-setuptools libatlas-base-dev -y")
    print("================== Completed Installing Setuptools and Libatlas ==================")

    print("================== Start Installing Fortran ==================")
    os.system("sudo apt install libatlas3-base libgfortran5 -y")
    print("================== Completed Installing Fortran ==================")

    print("================== Start Installing rpi_ws281x ==================")
    os.system("sudo pip3 install rpi_ws281x")
    print("================== Completed Installing rpi_ws281x ==================")

    print("================== Start Installing Apache ==================")
    os.system("sudo apt install apache2 -y")
    print("================== Completed Installing Apache ==================")

    print("================== Start Installing Mod WSGI ==================")
    os.system("sudo apt install libapache2-mod-wsgi-py3 -y")
    print("================== Completed Installing Mod WSGI ==================")


install_dependencies()

