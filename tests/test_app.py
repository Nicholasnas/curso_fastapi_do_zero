from fastapi.testclient import TestClient

from fast_zero.app import app

"""Seguindo a abordagem AAA"""
def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app)  # Arrange

    response = client.get('/')  # Act
    
    # Assert
    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}
