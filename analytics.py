# analytics.py

# Valori estimative de beneficii ecologice per KG reciclat
BENEFICII = {
    'hartie': {'copaci_salvati': 0.017, 'apa_salvata_litri': 26},
    'plastic': {'co2_evitat_kg': 1.5, 'petrol_salvat_litri': 1.9},
    'metal': {'energie_salvata_kwh': 4.0},
    'sticla': {'co2_evitat_kg': 0.3}
}

def calculeaza_total_pe_categorii(date):
    totaluri = {'hartie': 0, 'plastic': 0, 'metal': 0, 'sticla': 0}
    for inregistrare in date:
        cat = inregistrare['categorie']
        totaluri[cat] += inregistrare['cantitate_kg']
    return totaluri

def calculeaza_evolutie_saptamanala(date):
    evolutie = {}
    for inregistrare in date:
        sapt = inregistrare['saptamana']
        if sapt not in evolutie:
            evolutie[sapt] = 0
        evolutie[sapt] += inregistrare['cantitate_kg']
    return evolutie

def calculeaza_beneficii_totale(totaluri_categorii):
    raport_beneficii = {}
    for cat, cantitate in totaluri_categorii.items():
        if cantitate > 0:
            raport_beneficii[cat] = {}
            for beneficiu, factor in BENEFICII[cat].items():
                raport_beneficii[cat][beneficiu] = cantitate * factor
    return raport_beneficii