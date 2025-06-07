import pytest
from apis.login import LoginApi

BASE_URL = "https://your-api-url.com"

@pytest.fixture
def api():
    return LoginApi(BASE_URL)

def test_login_success(api):
    response = api.login("usuario", "contraseña123")
    assert response.status_code == 200
    assert "token" in response.json()