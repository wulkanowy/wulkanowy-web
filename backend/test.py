from fastapi.testclient import TestClient
from requests import head
from main import app

client = TestClient(app)
#Ustawienia dla wszystkich testów 
nick = "jan@fakelog.cf"
password = "jan123"
host = "fakelog.cf"
symbol = "powiatwulkanowy"
ssl = "false"
#Ustawienia dla test_login_incorrect i test_symbol_incorrect
nick_invalid = "cipanowie@pocz.pl"
password_invalid = "dupa123"
symbol_invalid = "warszawa"
def test_login_correct():
    login = client.post("/login",headers={"Content-Type": "application/json"},json={"username": nick, "password": password, "host": host, "symbol": symbol, "ssl": ssl},)
    global cookies, headars, student, school_id
    cookies = login.json()["vulcan_cookies"]
    headars = login.json()["students"][0]["headers"]
    student = login.json()["students"][0]["cookies"]
    school_id = login.json()["students"][0]["school_id"]
    assert login.status_code == 200
    #print(login.json())
    assert login.json()["symbol"] == "powiatwulkanowy"
    assert login.json()["host"] == "fakelog.cf"

def test_login_incorrect():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": nick_invalid, "password": password_invalid, "host": host, "symbol": symbol, "ssl": ssl},)
    assert response.status_code == 403
    #print(response.json())
    assert response.json() == {
        "detail": "Username or password is incorrect"
    }

def test_symbol_incorrect():
    response = client.post("/login",headers={"Content-Type": "application/json"},json={"username": nick, "password": password, "host": host, "symbol": symbol_invalid, "ssl": ssl},)
    assert response.status_code == 403
    #print(response.json())
    assert response.json() == {
        'detail': 'Symbol is incorrect'
    }

def test_notes():
    response = client.post("/uonetplus-uczen/notes",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl},)
    assert response.status_code == 200
    #print(response.json())
    assert response.json()['notes'][0]['teacher'] == 'Karolina Kowalska [AN]'
    assert response.json()['notes'][3]['content'] == 'Litwo! Ojczyzno moja! Ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko aż kędy pieprz rośnie gdzie podział się? szukać prawodawstwa.'

def test_grades():
    response = client.post("/uonetplus-uczen/grades",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl, "json": {"okres": 16}},)
    assert response.status_code == 200
    #print(response.json())
    assert response.json()["subjects"][0]["grades"][0]["teacher"] == 'Karolina Kowalska'
    assert response.json()["subjects"][0]["grades"][0]["symbol"] == 'Akt'
    #assert response.json()['grades'][3]['grade'] == '4'
    
def test_school_info():
    response = client.post("/uonetplus-uczen/school-info",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl},)
    assert response.status_code == 200
    #print(response.json())

def test_conference():
    response = client.post("/uonetplus-uczen/conferences",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl},)
    assert response.status_code == 200
    #print(response.json())

def test_mobile_access_registed():
    response = client.post("/uonetplus-uczen/mobile-access/get-registered-devices",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl},)
    assert response.status_code == 200
    #print(response.json())

def test_mobile_access_register():
    response = client.post("/uonetplus-uczen/mobile-access/register-device",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl},)
    assert response.status_code == 200
    #print(response.json())

def test_mobile_access_delete_registed():
    response = client.post("/uonetplus-uczen/mobile-access/delete-registered-device",headers={"Content-Type": "application/json"},json={"vulcan_cookies": cookies, "student": student, "school_id": school_id, "host": host, "symbol": symbol, "ssl": ssl, "json": {"id": 1}, "headers": headars,})
    #Nowa metoda testowania
    #if response.status_code == 404:
    #    print(response.json())
    #else:
    #    print("Test")
    assert response.status_code == 200
    #print(response.json())