#!/usr/bin/env python3

import subprocess


def _preprocess():

    # install pip3
    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'install', 'python3-pip', '-y'])

    # install django
    subprocess.run(['pip3', 'install', 'django'])


if __name__ == "__main__":
    _preprocess()
