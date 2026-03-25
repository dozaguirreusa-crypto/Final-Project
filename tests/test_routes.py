from app import app

def test_get_all_users():
    client = app.test_client()
    res = client.get("/users")
    assert res.status_code == 200

def test_get_user():
    client = app.test_client()
    res = client.get("/users/1")
    assert res.status_code == 200

def test_post_user():
    client = app.test_client()
    res = client.post("/users", json={"name": "Pepe", "email": "pepe@test.com"})
    assert res.status_code == 201

def test_update_user():
    client = app.test_client()
    res = client.put("/users/1", json={"name": "Nuevo", "email": "nuevo@test.com"})
    assert res.status_code == 200

def test_delete_user():
    client = app.test_client()
    res = client.delete("/users/1")
    assert res.status_code == 200
