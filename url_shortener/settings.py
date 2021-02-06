#can also call it as config file
import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)


SQLALCHEMY_DATABASE_URI = config.get('DATABASE_URL')
SQLALCHEMY_TRACK_MODIFICATIONS = False

ADMIN_USERNAME = config.get('ADMIN_USERNAME')
ADMIN_PASSWORD = config.get('ADMIN_PASSWORD')