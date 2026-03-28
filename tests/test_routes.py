from app import app


def test_home_page():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200


def test_users_list(mocker):
    mocker.patch(
        "src.models.UserModel.get_all",
        return_value=[]
    )

    client = app.test_client()
    res = client.get("/users")
    assert res.status_code == 200


def test_create_user_form():
    client = app.test_client()
    res = client.get("/users/create")
    assert res.status_code == 200


def test_create_user_post(mocker):
    mocker.patch("src.models.UserModel.create_user")

    client = app.test_client()
    res = client.post(
        "/users/create",
        data={"name": "Pepe", "email": "pepe@test.com"},
        follow_redirects=True
    )

    assert res.status_code == 200


def test_edit_user_form(mocker):
    mocker.patch(
        "src.models.UserModel.get_user",
        return_value={"id": 1, "name": "Pepe", "email": "pepe@test.com"}
    )

    client = app.test_client()
    res = client.get("/users/edit/1")
    assert res.status_code == 200


def test_update_user_post(mocker):
    mocker.patch(
        "src.models.UserModel.get_user",
        return_value={"id": 1, "name": "Pepe", "email": "pepe@test.com"}
    )
    mocker.patch("src.models.UserModel.update_user")

    client = app.test_client()
    res = client.post(
        "/users/edit/1",
        data={"name": "Nuevo", "email": "nuevo@test.com"},
        follow_redirects=True
    )

    assert res.status_code == 200


def test_delete_user(mocker):
    mocker.patch("src.models.UserModel.delete_user")

    client = app.test_client()
    res = client.post(
        "/users/delete/1",
        follow_redirects=True
    )

    assert res.status_code == 200