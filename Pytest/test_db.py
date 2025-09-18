import pytest
from db import save_user

'''
@pytest.fixture
def db():
    databae = Database()
    yield databae
    databae.data.clear()

def test_add_user(db):
    db.add_user(1, "Acob")
    assert db.get_user(1) == "Acob"

def test_add_duplicate(db):
    db.add_user(1, "Acob")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Acob")

def test_delete_user(db):
    db.add_user(2, "Bob")
    db.delete_user(2)
    assert db.get_user(2) is None
'''
def test_save_user(mocker):
    mock_conn = mocker.patch("sqlite3.connect")
    mock_cursor = mock_conn.return_value.cursor.return_value

    save_user("Alice", 30)

    mock_conn.assert_called_once_with("users.db")
    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30)
    )