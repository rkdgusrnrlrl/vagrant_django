#!/usr/bin/env python3

import subprocess


def _preprocess():
    subprocess.Popen(['pwd'])

    subprocess.run(['apt-get', 'update'])
    subprocess.run(['apt-get', 'install', 'python3-pip', '-y'])

    subprocess.run(['pip3', 'install', 'django'])


if __name__ == "__main__":
    _preprocess()
