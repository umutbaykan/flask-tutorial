import pytest
import json
from flask import g, session


def test_successful_login(client):
    data = {"username": "admiral_1", "password": "password"}
    with client:
        response = client.post(
            "/auth/login", data=json.dumps(data), content_type="application/json"
        )
        assert response.status_code == 200
        assert len(session["user_id"]) == 24


def test_successful_register(client, auth):
    data = {"username": "admiral_3", "password": "password"}
    with client:
        response = client.post(
            "/auth/register", data=json.dumps(data), content_type="application/json"
        )
        assert response.status_code == 201
        assert "user_id" in session


@pytest.mark.parametrize(
    ("username", "password", "error"),
    (
        ("", "", b"Username is required."),
        ("a", "", b"Password is required."),
        ("test", "test", b"Password is too short"),
        ("admiral_1", "password", b"Username already exists"),
        ("areallylongusername", "password", b"Username is too long"),
    ),
)
def test_register_validate_input(client, username, password, error):
    data = {"username": username, "password": password}
    response = client.post(
        "/auth/register", data=json.dumps(data), content_type="application/json"
    )
    assert error in response.data


@pytest.mark.parametrize(
    ("username", "password", "error"),
    (
        ("", "", b"Incorrect username."),
        ("admiral_1", "notright", b"Incorrect password."),
    ),
)
def test_login_validate_input(client, username, password, error):
    data = {"username": username, "password": password}
    response = client.post(
        "/auth/login", data=json.dumps(data), content_type="application/json"
    )
    assert error in response.data


def test_logout(client, auth):
    with client:
        auth.login()
        assert "user_id" in session
        auth.logout()
        assert "user_id" not in session
