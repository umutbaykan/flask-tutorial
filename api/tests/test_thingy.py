import pytest
from flask import g, session
from battleship.db import get_db


def test_user(web_client, app):
    response = web_client.get('/response/getme')
    response_data = response.json
    assert response.status_code == 200
    assert response_data["name"] == "Jonathan"
    # assert response == 200
    # with app.app_context():
    #     assert get_db().execute(
    #         "SELECT * FROM user WHERE username = 'a'",
    #     ).fetchone() is not None
