import os
import sys
import requests
from django import template
from django.utils.safestring import mark_safe
from django.shortcuts import render
import json
import requests
from django.shortcuts import redirect
from bs4 import BeautifulSoup

def get_notes(register_id, register_r, oun, s):
    cookies = {
        "biezacyRokSzkolny": f"{register_r.json()['data'][0]['DziennikRokSzkolny']}",
        "idBiezacyDziennik": f"{register_r.json()['data'][0]['IdDziennik']}",
        "idBiezacyDziennikPrzedszkole": f"{register_r.json()['data'][0]['IdPrzedszkoleDziennik']}",
        "idBiezacyDziennikWychowankowie": f"{register_r.json()['data'][0]['IdWychowankowieDziennik']}",
        "idBiezacyUczen": f"{register_r.json()['data'][0]['IdUczen']}"
    }

    notes = s.post(oun+'/UwagiIOsiagniecia.mvc/Get', cookies=cookies)

    notes_json = notes.json()

    with open('json/notes.json', 'w') as f:
        json.dump(notes_json, f)

def prepare_notes_for_display():
    with open('json/notes.json') as f:
        notes = json.load(f)

    i = 0
    
    print('------------------UWAGI------------------')
    while True:
        if notes['data']['Uwagi'] == []:
            print('Brak uwag!')
            break
        else:
            print('------------------------------------')
            print('Treść: '+notes['data']['Uwagi'][i]['TrescUwagi'])
            print('Kategoria: '+notes['data']['Uwagi'][i]['Kategoria'])
            print('Data: '+notes['data']['Uwagi'][i]['DataWpisu'])
            print('Nauczyciel: '+notes['data']['Uwagi'][i]['Nauczyciel'])
            print('Punkty: '+notes['data']['Uwagi'][i]['Punkty'])

            if notes['data']['Uwagi'][i] == notes['data']['Uwagi'][-1]:
                i = 0
                break
            i += 1
    
    print('------------------OSIĄGNIĘCIA------------------')
    while True:
        if notes['data']['Osiagniecia'] == []:
            print('Brak osiągnięć!')
            break
        else:
            print(notes['data']['Osiagniecia'][i])
            if notes['data']['Osiagniecia'][i] == notes['data']['Osiagniecia'][-1]:
                i = 0
                break
            i += 1
