import pytest
from fastapi.testclient import TestClient

from fast_zero.app import app

"""Seguindo a abordagem AAA"""


@pytest.fixture
def cliente():
    return TestClient(app)   # Arrange


def test_create_user_app(cliente):

    resposta = cliente.post(
        '/users/',
        json={
            'username': 'ricardo',
            'email': 'ricardo@gmail.com',
            'password': 'secret',
        },
    )

    assert resposta.status_code == 201
    assert resposta.json() == {
        'username': 'ricardo',
        'email': 'ricardo@gmail.com',
        'id': 1,
    }


def test_retorna_users_app(cliente):

    response = cliente.get('/users/')  # Act

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'ricardo',
                'email': 'ricardo@gmail.com',
            }
        ]
    }


def test_update_user_app(cliente):
    resposta = cliente.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@gmail.com',
            'password': 'newpassword',
        },
    )

    assert resposta.status_code == 200
    assert resposta.json() == {
        'username': 'bob',
        'email': 'bob@gmail.com',
        'id': 1,
    }


def test_delete_user_app(cliente):
    resposta = cliente.delete('/users/1')

    assert resposta.status_code == 200
    assert resposta.json() == {'detail': 'User deleted'}
