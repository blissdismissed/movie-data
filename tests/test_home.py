# test_home.py
from app import app

def test_home_page():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert b'Movie Search' in response.data
    