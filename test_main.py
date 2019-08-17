'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'SECRET'
TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYmYiOjE1NjU0NDc3NTMsImVtYWlsIjoiYWJkZWxhbGVlbUBnbXguY29tIiwiZXhwIjoxNTY2NjU3MzUzfQ.JGoYmZ18ofem2VAAss1JC5oQ9mc1heS4qFmrohz_MWY'
EMAIL = 'abdelaleem@gmx.com'
PASSWORD = 'Test123!!'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = True
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
