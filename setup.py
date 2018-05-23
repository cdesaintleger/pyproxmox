from distutils.core import setup
from setuptools import find_packages

setup(name='pyproxmox',
      version='1.0-b',
      description=('Proxmox API wrapper'),
      author='Daemonthread',
      url='https://github.com/Daemonthread/pyproxmox',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)
