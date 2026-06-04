# interfata.py
import data_manager
import analytics
import visualizer

def main():
    # Încărcăm datele existente la pornire
    date_aplicatie = data_manager.incarca_date()
    
    while True:
        print("=== APLICAȚIE EVIDENȚĂ RECICLARE ===")
        print("1. Adaugă o nouă colectare")
        print("2. Vezi raport text și beneficii ecologice")
        print("3. Vezi grafic: Total pe categorii")
        print("4. Vezi grafic: Evoluție pe săptămâni")
        print("5. Ieșire")
        
        optiune = input("Alege o opțiune: ")
        
        if optiune == '1':
            utilizator = input("Nume utilizator: ")
            locatie = input("Locație (ex: Corp A, Facultate): ")
            saptamana = input("Săptămâna (ex: S1, S2): ")
            categorie = input("Categorie (hartie/plastic/metal/sticla): ")
            cantitate_str = input("Cantitate (kg): ")
            
            valid, rezultat = data_manager.valideaza_intrare(categorie, cantitate_str)
            if valid:
                date_aplicatie = data_manager.adauga_inregistrare(
                    date_aplicatie, utilizator, locatie, saptamana, categorie, rezultat
                )
                print("-> Date adăugate cu succes!\n")
            else:
                print(f"-> EROARE: {rezultat}\n")
                
        elif optiune == '2':
            totaluri = analytics.calculeaza_total_pe_categorii(date_aplicatie)
            beneficii = analytics.calculeaza_beneficii_totale(totaluri)
            visualizer.afiseaza_raport_text(totaluri, beneficii)
            
        elif optiune == '3':
            totaluri = analytics.calculeaza_total_pe_categorii(date_aplicatie)
            visualizer.grafic_totaluri_categorii(totaluri)
            
        elif optiune == '4':
            evolutie = analytics.calculeaza_evolutie_saptamanala(date_aplicatie)
            visualizer.grafic_evolutie_saptamanala(evolutie)
            
        elif optiune == '5':
            print("La revedere!")
            break
        else:
            print("Opțiune invalidă. Încearcă din nou.\n")

if __name__ == "__main__":
    main()