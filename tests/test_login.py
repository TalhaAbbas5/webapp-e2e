def test_login_success(client):
    """Test valid login redirects to dashboard"""
    response = client.post("/", data={
        "username": "admin",
        "password": "1234"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Welcome! Login Successful" in response.data

def test_login_failure(client):
    """Test invalid login shows error message"""
    response = client.post("/", data={
        "username": "wrong",
        "password": "wrong"
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b"Invalid username or password" in response.data

def test_dashboard_requires_login(client):
    """Test accessing dashboard without login redirects to login page"""
    response = client.get("/dashboard", follow_redirects=True)
    assert response.status_code == 200
    assert b"Login" in response.data

