# -*- coding: utf-8 -*-

import os

# Configure flask and mongo connection
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'faeria-pandora-stats'
SERVER_NAME = None
X_DOMAINS = '*'

# Enable reads only of resources
RESOURCE_METHODS = ['GET']

# Enable reads only of items
ITEM_METHODS = ['GET']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRES = 20

# Override the default pagination, theres a lot of data to get at...
PAGINATION_LIMIT = 500
PAGINATION_DEFAULT = 100

# Expose the rating
rating = {
    # 'title' tag used in item links.
    'item_title': 'rating',

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'points': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 150,
            'required': True,
        },
        'level': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 10,
        },
        'ts': {
            'type': 'number',
        },
    }
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'ratings': rating
}