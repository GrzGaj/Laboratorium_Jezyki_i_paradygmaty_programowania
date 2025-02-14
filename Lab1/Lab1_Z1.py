
# problem podziału paczek
# programowanie proceduralne
def podziel_paczki(wagi,max_waga):
    #sortowanie paczki malejąco
    wagi_sort= sorted(wagi, reverse= True)
    kursy = []

    # sprawdzenie czy paczka nie przekracza wartości max
    for waga in wagi:
        if waga >max_waga:
            raise ValueError(f"Paczka o wadze {waga} przekracza maksymalną dozwoloną wagę kursu ({max_waga} kg.)")

# iteracja po dostępnych paczkach
    for waga in wagi_sort:
        dodano = False
# szukanie kursu do którego można dodać paczke
        for kurs in kursy:
            if sum(kurs)+ waga <=max_waga:
                kurs.append(waga)
                dodano = True
                break
# jeżeli nie można dodać paczki do żadnego kursu utwórzy nowy kurs
        if not dodano:
            kursy.append([waga])

    return len(kursy), kursy

if __name__ == "__main__":
    wagi = [10,15,7,20,5,8,10]
    max_waga = 25
    liczba_kursow, kursy = podziel_paczki(wagi, max_waga)
    print(f"Liczba kursów:{liczba_kursow}")
    for i, kurs in enumerate(kursy,1):
        print(f"Kursy {i}: {kurs} - suma wag: {sum(kurs)} kg")
