#!/bin/bash
# post installing script for Ubuntu 14.04 Trusty Tahr Desktop
#
# Check for Updates
sudo apt-get -y update
# Upgrade Packages
sudo apt-get -y upgrade

# install python 
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python2.7

# install python libraries
sudo apt-get install -y python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
