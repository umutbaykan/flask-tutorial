import os
import glob
import json
import pytest
from battleship import create_app
from battleship.db import seed_test_database

@pytest.fixture
def app():
    app = create_app({
        'TESTING': True,
        'MONGO_URI': 'mongodb://0.0.0.0/battleship-test',
    })

    # iterating through the seeds folder to populate the DB in every test
    with app.app_context():
        seed_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seeds')
        for file_path in glob.glob(os.path.join(seed_path, '*')):
            if os.path.isfile(file_path):
                collection = os.path.basename(file_path).split('.')[0]
                with open(file_path, 'r') as f:
                    data = json.load(f)
                    seed_test_database(collection, data)
        
    yield app


@pytest.fixture
def app_context(app):
    with app.app_context():
        yield


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()


class AuthActions(object):
    def __init__(self, client):
        self._client = client

    def login(self, username='admiral_1', password='password'):
        data={'username': username, 'password': password}
        return self._client.post(
            '/auth/login', data=json.dumps(data), content_type='application/json'
        )

    def logout(self):
        return self._client.get('/auth/logout')


@pytest.fixture
def auth(client):
    return AuthActions(client)