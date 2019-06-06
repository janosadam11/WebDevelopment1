import pytest, os
from Lesson_22.main import app

@pytest.fixture()
def client():
    app.config["TESTING"] = True
    os.environ["TESTING"] = "1"
    client = app.test_client()
    yield client

def test_index_not_logged_in(client):
    response = client.get('/')
    assert b'Enter your name' in response.data