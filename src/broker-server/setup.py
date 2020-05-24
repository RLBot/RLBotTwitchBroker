# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "rlbot_twitch_broker_server"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="RLBot Twitch Broker",
    author_email="rlbotofficial@gmail.com",
    url="",
    keywords=["Swagger", "RLBot Twitch Broker"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['rlbot_twitch_broker_server=rlbot_twitch_broker_server.__main__:main']},
    long_description="""\
    Allows custom Rocket League bots to register themselves with a central broker.
    """
)
