def test_admin_dashboard(client):
    login = client.post(
        "/auth/login",
        data={
            "username": "admin@agendamento.com",
            "password": "admin123"
        },
    )

    assert login.status_code == 200
    token = login.json()["access_token"]
    response = client.get(
        "/admin/dashboard",
        headers={
            "Authorization": f"Bearer {token}"
        },
    )

    assert response.status_code == 200


def test_admin_dashboard_access_as_admin(client, admin_token):
    response = client.get(
        "/admin/dashboard",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200