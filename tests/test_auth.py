def test_login_admin(client):
    response = client.post(
        "/auth/login",
        data={
            "username": "admin@admin.com",
            "password": "admin123"
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert "access_token" in body
