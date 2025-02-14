def analiza(data):
    #Analizuje niejednorodne dane i zwraca ekstremalne wartości
    numbers = list(filter(lambda x: isinstance(x, (int, float)), data))
    strings = list(filter(lambda x: isinstance(x, str), data))
    tuples = list(filter(lambda x: isinstance(x, tuple), data))
    
    max_number = max(numbers, default=None)
    longest_string = max(strings, key=len, default=None)
    largest_tuple = max(tuples, key=len, default=None)
    
    return {
        "Największa liczba": max_number,
        "Najdłuższy tekst": longest_string,
        "Największa krotka": largest_tuple
    }

data = [10, "hello", (1, 2, 3), 3.14, "world", (1, 2, 3, 4), 100]
print(analiza(data))
