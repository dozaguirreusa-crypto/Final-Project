import pytest
from src.models import UserModel

def test_create_user(mocker):
    mocker.patch("src.models.get_connection")
    UserModel.create_user("Test", "test@test.com")

def test_get_user(mocker):
    mocker.patch("src.models.get_connection")
    UserModel.get_user(1)

def test_get_all(mocker):
    mocker.patch("src.models.get_connection")
    UserModel.get_all()

def test_update_user(mocker):
    mocker.patch("src.models.get_connection")
    UserModel.update_user(1, "New", "new@test.com")

def test_delete_user(mocker):
    mocker.patch("src.models.get_connection")
    UserModel.delete_user(1)
