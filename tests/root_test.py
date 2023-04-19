
def test_root(client):
    expected_response = {
        "status": "ok"
    }

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == expected_response