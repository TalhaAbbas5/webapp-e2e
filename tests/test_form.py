def test_form_success(client):
    # First, login
    client.post("/", data={"username": "admin", "password": "1234"})

    # Submit valid form
    response = client.post("/form", data={
        "name": "John Doe",
        "email": "john@example.com",
        "age": "30"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Form submitted successfully!" in response.data

def test_form_missing_fields(client):
    client.post("/", data={"username": "admin", "password": "1234"})

    response = client.post("/form", data={
        "name": "",
        "email": "john@example.com",
        "age": "30"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"All fields are required" in response.data

def test_form_invalid_email(client):
    client.post("/", data={"username": "admin", "password": "1234"})

    response = client.post("/form", data={
        "name": "John",
        "email": "invalidemail",
        "age": "30"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid email address" in response.data

def test_form_invalid_age(client):
    client.post("/", data={"username": "admin", "password": "1234"})

    response = client.post("/form", data={
        "name": "John",
        "email": "john@example.com",
        "age": "-5"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Age must be a positive number" in response.data

