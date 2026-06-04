# visualizer.py
import matplotlib.pyplot as plt

def afiseaza_raport_text(totaluri, beneficii):
    print("\n--- RAPORT DE PERFORMANȚĂ ECOLOGICĂ ---")
    for cat, total in totaluri.items():
        print(f"[{cat.upper()}]: {total} kg colectate")
        if cat in beneficii:
            for ben, val in beneficii[cat].items():
                print(f"  -> {ben.replace('_', ' ').capitalize()}: {val:.2f}")
    print("---------------------------------------\n")

def grafic_totaluri_categorii(totaluri):
    categorii = list(totaluri.keys())
    cantitati = list(totaluri.values())
    
    plt.bar(categorii, cantitati, color=['blue', 'orange', 'gray', 'green'])
    plt.title('Total Deșeuri Colectate pe Categorii')
    plt.xlabel('Categorie')
    plt.ylabel('Cantitate (kg)')
    plt.savefig("grafic_categorii.png")
    print("-> Graficul a fost salvat ca 'grafic_categorii.png'. Caută-l în stânga!")
    plt.close()

def grafic_evolutie_saptamanala(evolutie):
    saptamani = sorted(list(evolutie.keys()))
    cantitati = [evolutie[s] for s in saptamani]
    
    plt.plot(saptamani, cantitati, marker='o', linestyle='-', color='g')
    plt.title('Evoluția Colectării pe Săptămâni')
    plt.xlabel('Săptămâna')
    plt.ylabel('Total Cantitate (kg)')
    plt.grid(True)
   plt.savefig("grafic_evolutie.png")
    print("-> Graficul a fost salvat ca 'grafic_evolutie.png'. Caută-l în stânga!")
    plt.close()