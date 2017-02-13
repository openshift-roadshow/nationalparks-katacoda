from __future__ import print_function

import os
import json

from flask import Flask, request
from flask_restful import Resource, Api

application = Flask(__name__)

api = Api(application)

class HealthCheck(Resource):
    def get(self):
        return 'OK'

api.add_resource(HealthCheck, '/ws/healthz/')

class Info(Resource):
    description = {
        'id': 'nationalparks-py',
        'displayName': 'National Parks (PY)',
        'type': 'cluster',
        'center': {'latitude': '47.039304', 'longitude': '14.505178'},
        'zoom': 4
    }

    def get(self):
        return self.description

api.add_resource(Info, '/ws/info/')

def format_result(entries):
    result = []

    for entry in entries:
        data = {}

        data['id'] = entry['name']
        data['latitude'] = str(entry['coordinates'][0])
        data['longitude'] = str(entry['coordinates'][1])
        data['name'] = entry['toponymName']

        result.append(data)

    return result

DATASET_FILE = 'nationalparks.json'

dataset = []

def load_data(filename):
    global dataset

    dataset = []

    with open(filename, 'r') as fp:
        for data in fp.readlines():
            dataset.append(json.loads(data))

    return len(dataset)

load_data(DATASET_FILE)

class DataLoad(Resource):
    def get(self):
        count = load_data(DATASET_FILE)
        return 'Inserted %s items.' % count

api.add_resource(DataLoad, '/ws/data/load')

class DataAll(Resource):
    def get(self):
        return format_result(dataset)

api.add_resource(DataAll, '/ws/data/all')

@application.route('/')
def index():
    return 'Welcome to the National Parks data service.'
