#!/usr/bin/env bash

apt install -y python3 python3-pip python3-dev

# add-apt-repository ppa:deadsnakes/ppa
# apt install -y python3.9
# apt install -y python3.9-distutils

# python3.9 -m pip install pip

# python3.9 -m pip install -r /autograder/source/requirements.txt
python3 -m pip install -r /autograder/source/requirements.txt
