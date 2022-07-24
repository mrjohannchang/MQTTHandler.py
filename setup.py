# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os
import re

with open(os.path.join('mqtthandler', 'version.py')) as f:
  exec(f.readline())

setup(
  name='mqtthandler',
  version=__version__,
  description='A Python logging handler using MQTT protocol',
  author='Johann Chang',
  author_email='mr.changyuheng@gmail.com',
  url='https://github.com/changyuheng/MQTTHandler.py',
  license='MPL-2.0',
  packages=['mqtthandler'],
  install_requires=['paho-mqtt'],
)
