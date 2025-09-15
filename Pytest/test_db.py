import pytest
from db import Database

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