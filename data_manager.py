# data_manager.py
import json
import os

FISIER_DATE = "deseuri.json"
CATEGORII_VALIDE = ['hartie', 'plastic', 'metal', 'sticla']

def incarca_date():
    if not os.path.exists(FISIER_DATE):
        return []
    with open(FISIER_DATE, 'r') as f:
        return json.load(f)

def salveaza_date(date):
    with open(FISIER_DATE, 'w') as f:
        json.dump(date, f, indent=4)

def valideaza_intrare(categorie, cantitate):
    if categorie.lower() not in CATEGORII_VALIDE:
        return False, "Categoria trebuie să fie hârtie, plastic, metal sau sticlă."
    try:
        val = float(cantitate)
        if val <= 0:
            return False, "Cantitatea trebuie să fie un număr pozitiv."
        return True, val
    except ValueError:
        return False, "Cantitatea trebuie să fie un număr valid."

def adauga_inregistrare(date, utilizator, locatie, saptamana, categorie, cantitate):
    noua_inregistrare = {
        "utilizator": utilizator,
        "locatie": locatie,
        "saptamana": saptamana,
        "categorie": categorie.lower(),
        "cantitate_kg": cantitate
    }
    date.append(noua_inregistrare)
    salveaza_date(date)
    return date