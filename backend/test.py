from errno import errorcode
from fastapi.testclient import TestClient
from main import app
import pytest
import json
client = TestClient(app)
class fg:
    lightgreen = '\x1B[38;5;46m'
    orange = '\x1B[38;5;208m'
    red = '\x1B[38;5;160m'
    rs = '\033[0m'
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
    #print(login.json())
    if login.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(login.status_code) + fg.rs)
        assert login.json()["symbol"] == "powiatwulkanowy"
        assert login.json()["host"] == "fakelog.cf"
    elif login.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(login.status_code) + fg.rs)
        formatted_string = json.dumps(login.json(), indent=4)
        print(formatted_string)
    elif login.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(login.status_code) + fg.rs)
    elif login.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(login.status_code) + fg.rs)
    elif login.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(login.status_code) + fg.rs)
    elif login.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(login.status_code) + fg.rs)
        formatted_string = json.dumps(login.json(), indent=4)
        print(formatted_string)
    elif login.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(login.status_code) + fg.rs)
        formatted_string = json.dumps(login.json(), indent=4)
        print(formatted_string)
    elif login.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(login.status_code) + fg.rs)
    elif login.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(login.status_code) + fg.rs)
    elif login.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(login.status_code) + fg.rs)
    elif login.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(login.status_code) + fg.rs)
    if not cookies:
        global errorcode
        errorcode = 1
        print("\nCookies output: ")
        print(login.json()["vulcan_cookies"])
        pytest.fail("No VULCAN cookies detected")
    elif not headars:
        errorcode = 2
        print("\nHeaders output: ")
        print(login.json()["students"][0]["headers"])
        pytest.fail("No headers detected")
    elif not student:
        errorcode = 3
        print("\nStudent output: ")
        print(login.json()["students"][0]["cookies"])
        pytest.fail("No student cookies detected")
    elif not school_id:
        errorcode = 4
        print("\nSchool ID output: ")
        print(login.json()["students"][0]["school_id"])
        pytest.fail("No school ID detected")


def test_login_incorrect():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
        assert response.json() == {"detail": "Username or password is incorrect"}
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())


def test_symbol_incorrect():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
        assert response.json() == {"detail": "Symbol is incorrect"}
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())


def test_notes():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()["notes"][0]["teacher"] == "Karolina Kowalska [AN]"
        assert (
        response.json()["notes"][3]["content"]
        == "Litwo! Ojczyzno moja! Ty jesteś jak zdrowie. Ile cię trzeba cenić, ten tylko aż kędy pieprz rośnie gdzie podział się? szukać prawodawstwa."
        )
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())

def test_grades():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()["subjects"][0]["grades"][0]["teacher"] == "Karolina Kowalska"
        assert response.json()["subjects"][0]["grades"][0]["symbol"] == "Akt"
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())
    #assert response.json()['grades'][3]['grade'] == '4'


def test_school_info():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()["school"]["name"] == "Publiczna szkoła Wulkanowego nr 1 w fakelog.cf"
        assert response.json()["teachers"][0]["name"] == "Karolina Kowalska [AN]"
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())

def test_conference():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")   
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()[0]["subject"] == "Podsumowanie I semestru - średnia klasy, oceny, frekwencja, zachowanie."
        assert response.json()[1]["date"] == "06.09.2019 16:30"
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())

def test_mobile_access_registed():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()[0]["name"] == "To Be Filled By O.E.M.#To Be Filled By O.E.M. (Windows 8.1)"
        assert response.json()[1]["id"] == 1234
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())

def test_mobile_access_register():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()["pin"] == "999999"
        assert response.json()["qr_code_image"]
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())

def test_mobile_access_delete_registed():
    if errorcode == 1:
        pytest.skip("Skipped due to no cookies detected")
    elif errorcode == 2:
        pytest.skip("Skipped due to no headers detected")
    elif errorcode == 3:
        pytest.skip("Skipped due to no student cookies detected")
    elif errorcode == 4:
        pytest.skip("Skipped due to no school ID detected")
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
    if response.status_code == 200:
        print("\n" + fg.lightgreen + "OK " + str(response.status_code) + fg.rs)
        assert response.json()["success"] == True
    elif response.status_code == 400:
        print("\n" + fg.red + "Bad Request " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 401:
        print("\n" + fg.red + "Unauthorized " + str(response.status_code) + fg.rs)
    elif response.status_code == 403:
        print("\n" + fg.red + "Forbidden " + str(response.status_code) + fg.rs)
    elif response.status_code == 404:
        print("\n" + fg.orange + "Not Found " + str(response.status_code) + fg.rs)
    elif response.status_code == 405:
        print("\n" + fg.red + "Method Not Allowed " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 422:
        print("\n" + fg.red + "Unprocessable Entity " + str(response.status_code) + fg.rs)
        formatted_string = json.dumps(response.json(), indent=4)
        print(formatted_string)
    elif response.status_code == 500:
        print("\n" + fg.orange + "Internal Server Error " + str(response.status_code) + fg.rs)
    elif response.status_code == 502:
        print("\n" + fg.orange + "Bad Gateway " + str(response.status_code) + fg.rs)
    elif response.status_code == 503:
        print("\n" + fg.orange + "Service Unavailable " + str(response.status_code) + fg.rs)
    elif response.status_code == 504:
        print("\n" + fg.orange + "Gateway Timeout " + str(response.status_code) + fg.rs)
    #print(response.json())