# algorytm plecakowy funkcyjnie
def pakowanie_fun(pojemnosc, rzeczy):

    def pakowanie_ex(n, potrzebna_pojemnosc):
        # Bazowy przypadek: brak przedmiotów lub brak miejsca
        if n == 0 or potrzebna_pojemnosc == 0:
            return 0, []

        waga, wartosc = rzeczy[n - 1]
        if waga > potrzebna_pojemnosc:
            # Przedmiot za ciężki, pomijamy go
            return pakowanie_ex(n - 1, potrzebna_pojemnosc)

        # Rozważamy dwa przypadki: nie bierzemy lub bierzemy przedmiot
        puste = pakowanie_ex(n - 1, potrzebna_pojemnosc)
        dodaj_rzecz = pakowanie_ex(n - 1, potrzebna_pojemnosc - waga)
        dodaj_rzecz = (dodaj_rzecz[0] + wartosc, dodaj_rzecz[1] + [(waga, wartosc)])

        return max(puste, dodaj_rzecz, key=lambda x: x[0])

    maksimum, wybrane_rzeczy = pakowanie_ex(len(rzeczy), pojemnosc)
    return maksimum, wybrane_rzeczy


if __name__ == "__main__":
    pojemnosc = 50
    rzeczy = [(10, 60), (20, 100), (30, 120)]  # (waga, wartość)
    
    maksimum, wybrane = pakowanie_fun(pojemnosc, rzeczy)
    print(f"Maksymalna wartość: {maksimum}")
    print(f"Wybrane przedmioty: {wybrane}")
