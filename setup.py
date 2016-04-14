# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re

with open(os.path.join('mqtthandler', 'version.py')) as f:
  __version__ = re.sub(r"^.*'", '', re.sub(r"'$", '', f.readline().strip()))

setup(
  name='mqtthandler',
  version=__version__,
  description='A Python logging handler using MQTT protocol',
  author='Chang Yu-heng',
  author_email='mr.changyuheng@gmail.com',
  url='https://github.com/changyuheng/MQTTHandler',
  license='MIT',
  packages=['mqtthandler'],
  install_requires=['paho-mqtt'],
)
