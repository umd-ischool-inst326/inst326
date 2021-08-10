#!/usr/bin/env bash

apt install -y python3 python3-pip python3-dev

# add-apt-repository ppa:deadsnakes/ppa
# apt install -y python3.9
# apt install -y python3.9-distutils
# apt install -y python3-testresources

python3 -m pip install --upgrade pip
# python3 -m pip install --upgrade setuptools
# python3 -m pip install --upgrade distlib

python3 -m pip install -r /autograder/source/requirements.txt
