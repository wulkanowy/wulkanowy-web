from errno import errorcode
from fastapi.testclient import TestClient
from pyparsing import empty
from main import app
from sty import fg, bg, ef, rs, Style, RgbFg
import pytest
client = TestClient(app)
fg.orange = Style(RgbFg(255, 150, 50))
fg.lightgreen = Style(RgbFg(144, 238, 144))

# Ustawienia dla wszystkich testów
nick = "jan@fakelog.cf"
password = "jan123"
host = "fakelog.cf"
symbol = "powiatwulkanowy"
ssl = "false"
# Ustawienia tygodni dla testów
week_grades = "16"
# Ustawienia id dla testów
id_mobile_deleted = 1234
# Ustawienia dla test_login_incorrect i test_symbol_incorrect
nick_invalid = "jan@fakelog.cf"
password_invalid = "Jan321"
symbol_invalid = "warszawa"


def test_login_correct():
    login = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={"username": nick, "password": password, "host": host, "symbol": symbol, "ssl": ssl},
    )
    global cookies, headars, student, school_id
    cookies = login.json()["vulcan_cookies"]
    headars = login.json()["students"][0]["headers"]
    student = login.json()["students"][0]["cookies"]
    school_id = login.json()["students"][0]["school_id"]
    assert login.status_code == 200
    #print(login.json())
    if len(cookies) == 0:
        #print(fg.lightgreen + "OK" + login.status_code + rs)
        global errorcode
        errorcode = 1
        print("\nCookies output: ")
        print(login.json()["vulcan_cookies"])
        pytest.skip("No VULCAN cookies detected")
    else:
        #print(fg.orange + "OK" + login.status_code + rs)
        assert login.status_code == 200
    assert login.json()["symbol"] == "powiatwulkanowy"
    assert login.json()["host"] == "fakelog.cf"


def test_login_incorrect():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={
            "username": nick_invalid,
            "password": password_invalid,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {},
            "headers": headars,
        },
    )
    assert response.status_code == 403
    #print(response.json())
    assert response.json() == {"detail": "Username or password is incorrect"}


def test_symbol_incorrect():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/login",
        headers={"Content-Type": "application/json"},
        json={
            "username": nick,
            "password": password,
            "host": host,
            "symbol": symbol_invalid,
            "ssl": ssl,
            "json": {},
            "headers": headars,
        },
    )
    assert response.status_code == 403
    #print(response.json())
    assert response.json() == {"detail": "Symbol is incorrect"}


def test_notes():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/uonetplus-uczen/notes",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {},
            "headers": headars,
        },
    )
    assert response.status_code == 200
    #print(response.json())
    assert response.json()["notes"][0]["teacher"] == "Karolina Kowalska [AN]"
    assert (
        response.json()["notes"][3]["content"]
        == "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko aż kędy pieprz rośnie gdzie podział się? szukać prawodawstwa."
    )


def test_grades():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/uonetplus-uczen/grades",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {"okres": week_grades},
            "headers": headars,
        },
    )
    assert response.status_code == 200
    #print(response.json())
    assert response.json()["subjects"][0]["grades"][0]["teacher"] == "Karolina Kowalska"
    assert response.json()["subjects"][0]["grades"][0]["symbol"] == "Akt"
    #assert response.json()['grades'][3]['grade'] == '4'


def test_school_info():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/uonetplus-uczen/school-info",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {},
            "headers": headars,
        },
    )
    assert response.status_code == 200
    #print(response.json())
    assert response.json()["school"]["name"] == "Publiczna szkoła Wulkanowego nr 1 w fakelog.cf"
    assert response.json()["teachers"][0]["name"] == "Karolina Kowalska [AN]"


def test_conference():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")   
    response = client.post(
        "/uonetplus-uczen/conferences",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {},
            "headers": headars,
        },
    )
    assert response.status_code == 200
    #print(response.json())
    assert response.json()[0]["subject"] == "Podsumowanie I semestru - średnia klasy, oceny, frekwencja, zachowanie."
    assert response.json()[1]["date"] == "06.09.2019 16:30"

def test_mobile_access_registed():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/uonetplus-uczen/mobile-access/get-registered-devices",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {},
            "headers": headars,
        },
    )
    assert response.status_code == 200
    #print(response.json())
    assert response.json()[0]["name"] == "To Be Filled By O.E.M.#To Be Filled By O.E.M. (Windows 8.1)"
    assert response.json()[1]["id"] == 1234


def test_mobile_access_register():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    response = client.post(
        "/uonetplus-uczen/mobile-access/register-device",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
        },
    )
    assert response.status_code == 200
    #print(response.json())
    assert response.json()["pin"] == "999999"
    assert response.json()["qr_code_image"]

def test_mobile_access_delete_registed():
    if errorcode == 1:
        pytest.fail("Skipped due to no cookies detected")
    response = client.post(
        "/uonetplus-uczen/mobile-access/delete-registered-device",
        headers={"Content-Type": "application/json"},
        json={
            "vulcan_cookies": cookies,
            "student": student,
            "school_id": school_id,
            "host": host,
            "symbol": symbol,
            "ssl": ssl,
            "json": {"id": id_mobile_deleted},
            "headers": headars,
        },
    )
    # Nowa metoda testowania
    # if response.status_code == 404:
    #    print(response.json())
    # else:
    #    print("Test")
    assert response.status_code == 200
    #print(response.json())
    assert response.json()["success"] == True
    #assert response.json()["data"]
def test_workflow_code_return():
    if errorcode == 1:
        pytest.fail("Skipped due to no cookies detected")