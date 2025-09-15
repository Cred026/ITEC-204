from main import Usermanager
import pytest

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
