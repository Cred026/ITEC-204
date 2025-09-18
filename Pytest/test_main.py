from main import get_weather_data
import pytest

'''
@pytest.fixture
def user_manager():
    return Usermanager()

def test_add_user(user_manager):
    assert user_manager.add_users("john_doe", "john@example.con") == True
    assert user_manager.get_user("john_doe") == "john@example.con"

def test_add_duplicate_user(user_manager):
    user_manager.add_users("john_doe", "john@example.com")
    with pytest.raises(ValueError):
        user_manager.add_users("john_doe", "examplejohn@example.com")
'''

'''
@pytest.mark.parametrize("num, expected", [
    (1, False),
    (2, True),
    (3, True),
    (4, False),
    (17, True),
    (18, False),
    (19, True),
    (25, False),
])
def test_is_prime(num, expected):
    assert is_prime(num) == expected
'''

'''
def test_get_weather_data(mocker):
    mock_get = mocker.patch("main.requests.get")

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature": 25, "condiiton": "Sunny"}

    result = get_weather_data("Dubai")

    assert result == {"temperature": 25, "condiiton": "Sunny"}
    mock_get.assert_called_once_with("httpl://api.weather.com/v1/Dubai")
'''