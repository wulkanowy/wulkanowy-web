from fastapi.testclient import TestClient
import json
from main import app

client = TestClient(app)


#def test_read_item():
    #response = client.post("/login", headers={"Content-Type": "application/json"})
    #assert response.status_code == 405
    #assert response.json() == {
        #"id": "foo",
        #"title": "Foo",
        #"description": "There goes my hero",
    #}

def test_create_item():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": "jan@fakelog.cf", "password": "jan123", "host": "fakelog.cf", "symbol": "powiatwulkanowy", "ssl": "false"},)
    assert response.status_code == 200
    assert response.json()["symbol"] == "powiatwulkanowy"
    assert response.json()["host"] == "fakelog.cf"
    ciastka = response.json()["vulcan_cookies"]
    #print(ciastka)