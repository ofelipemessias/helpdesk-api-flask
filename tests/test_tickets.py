def test_create_ticket_returns_201(client):
    r = client.post("/tickets", json={"title": "Computador não liga", "priority": "high"})
    assert r.status_code == 201
    body = r.get_json()
    assert body["title"] == "Computador não liga"
    assert body["status"] == "open"
    assert body["priority"] == "high"
    assert "id" in body and "created_at" in body


def test_create_ticket_without_title_returns_400(client):
    r = client.post("/tickets", json={"description": "sem título"})
    assert r.status_code == 400


def test_create_ticket_with_invalid_priority_returns_400(client):
    r = client.post("/tickets", json={"title": "x", "priority": "urgentíssimo"})
    assert r.status_code == 400


def test_list_tickets_and_filter_by_status(client):
    client.post("/tickets", json={"title": "ticket 1"})
    client.post("/tickets", json={"title": "ticket 2"})
    r = client.get("/tickets")
    assert r.status_code == 200
    assert len(r.get_json()) == 2
    r = client.get("/tickets?status=closed")
    assert r.status_code == 200
    assert r.get_json() == []


def test_list_tickets_invalid_status_filter_returns_400(client):
    r = client.get("/tickets?status=inexistente")
    assert r.status_code == 400


def test_get_ticket_by_id_and_404(client):
    created = client.post("/tickets", json={"title": "impressora offline"}).get_json()
    r = client.get(f"/tickets/{created['id']}")
    assert r.status_code == 200
    assert r.get_json()["title"] == "impressora offline"
    assert client.get("/tickets/9999").status_code == 404


def test_update_ticket_status_flow(client):
    created = client.post("/tickets", json={"title": "e-mail não envia"}).get_json()
    r = client.patch(f"/tickets/{created['id']}", json={"status": "in_progress"})
    assert r.status_code == 200
    assert r.get_json()["status"] == "in_progress"
    r = client.patch(f"/tickets/{created['id']}", json={"status": "closed"})
    assert r.get_json()["status"] == "closed"


def test_update_ticket_invalid_status_returns_400(client):
    created = client.post("/tickets", json={"title": "mouse quebrado"}).get_json()
    r = client.patch(f"/tickets/{created['id']}", json={"status": "congelado"})
    assert r.status_code == 400


def test_update_nonexistent_ticket_returns_404(client):
    assert client.patch("/tickets/9999", json={"status": "closed"}).status_code == 404


def test_delete_ticket(client):
    created = client.post("/tickets", json={"title": "monitor sem imagem"}).get_json()
    assert client.delete(f"/tickets/{created['id']}").status_code == 204
    assert client.get(f"/tickets/{created['id']}").status_code == 404
