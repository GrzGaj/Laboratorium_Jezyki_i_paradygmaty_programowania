import numpy as np
from functools import reduce

def apply_operation(matrices, operation):
    return reduce(lambda a, b: eval(operation, {"a": a, "b": b, "np": np}), matrices)

# Przykładowe macierze
matrices = [
    np.array([[1, 2], [3, 4]]),
    np.array([[5, 6], [7, 8]]),
    np.array([[9, 10], [11, 12]])
]

# Wybór operacji przez użytkownika
print("Wybierz operację: 'a + b' (sumowanie), 'a @ b' (mnożenie) lub podaj własną:")
user_operation = input("Podaj operację: ")

# Przetwarzanie macierzy
result = apply_operation(matrices, user_operation)

print("Wynikowa macierz:")
print(result)
