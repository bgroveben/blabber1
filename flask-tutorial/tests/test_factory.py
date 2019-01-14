from flaskr import create_app

def test_config():
    """
    The only thing we need to test in the factory is the configuration.
    The only behavior that can change is passing test config.
    """
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    """
    This test checks that the response data matches.
    """
    response = client.get('/hello')
    assert response.data == b'Hello, World!'
