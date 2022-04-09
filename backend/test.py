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

def test_login_correct():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": "jan@fakelog.cf", "password": "jan123", "host": "fakelog.cf", "symbol": "powiatwulkanowy", "ssl": "false"},)
    assert response.status_code == 200
    assert response.json()["symbol"] == "powiatwulkanowy"
    assert response.json()["host"] == "fakelog.cf"
    ciastka1 = response.json()["vulcan_cookies"]
    #print(ciastka)

def test_login_incorrect():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": "cipanowie@pocz.pl", "password": "dupa123", "host": "fakelog.cf", "symbol": "powiatwulkanowy", "ssl": "false"},)
    assert response.status_code == 403
    print(response.json())
    assert response.json() == {
        "detail": "Username or password is incorrect"
    }
    #assert response.html()["host"] == "fakelog.cf"
    #ciastka = response.json()["vulcan_cookies"]
    #print(ciastka)

def test_symbol_incorrect():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": "jan@fakelog.cf", "password": "jan123", "host": "fakelog.cf", "symbol": "warszawa", "ssl": "false"},)
    assert response.status_code == 403
    print(response.json())
    assert response.json() == {
        'detail': 'Symbol is incorrect'
    }

def test_notes():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": "jan@fakelog.cf", "password": "jan123", "host": "fakelog.cf", "symbol": "powiatwulkanowy", "ssl": "false"},)
    ciastka = response.json()["vulcan_cookies"]
    response = client.post("/uonetplus-uczen/notes",headers={"Content-Type": "application/json"},json={{"vulcan_cookies": ciastka, "student": {"idBiezacyDziennik": "15", "idBiezacyUczen": "1", "idBiezacyDziennikPrzedszkole": "0", "biezacyRokSzkolny": "2018"}, "school_id": "123456", "host": "fakelog.cf", "symbol": "powiatwulkanowy","ssl": "false"}},)
    assert response.status_code == 200
    print(response.json())
    assert response.json() == {
        'detail': 'Symbol is incorrect'
    }