#Harmonogramowanie Zadań z Ograniczeniami - proceduralnie
from typing import List, Tuple

def harmonogram_proceduralnie(tasks: List[Tuple[int, int, int]]) -> Tuple[int, List[Tuple[int, int, int]]]:

    # Sortowanie zadań według czasu zakończenia
    tasks.sort(key=lambda x: x[1])
    
    wybierz_zadanie = []
    nagroda = 0
    czas = 0
    
    for start, end, reward in tasks:
        if start >= czas:  
            wybierz_zadanie.append((start, end, reward))
            nagroda += reward
            czas = end
    
    return nagroda, wybierz_zadanie

if __name__ == "__main__":

    tasks = [(1, 3, 5), (2, 5, 6), (4, 6, 5), (6, 7, 4), (5, 8, 11), (7, 9, 2)]
    nagroda_proc, wybierz_zadanie_proc = harmonogram_proceduralnie(tasks)
    print("Procedural:", nagroda_proc, wybierz_zadanie_proc)