# algorytm plecakowy proceduralnie
def pakowanie(pojemnosc, rzeczy): 
    n = len(rzeczy)

    dp = [[0 for _ in range(pojemnosc + 1)] for _ in range(n + 1)]
    
    # Budowanie tablicy dp
    for i in range(1, n + 1):
        for w in range(pojemnosc + 1):
            weight, value = rzeczy[i - 1]
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # przedmioty
    w = pojemnosc
    wybrane_rzeczy = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            wybrane_rzeczy.append(rzeczy[i - 1])
            w -= rzeczy[i - 1][0]

    return dp[n][pojemnosc], wybrane_rzeczy


if __name__ == "__main__":
    pojemnosc = 50
    rzeczy = [(10, 60), (20, 100), (30, 120)]  # (waga, wartość)
    
    max, wybrane = pakowanie(pojemnosc, rzeczy)
    print(f"Maksymalna wartość: {max}")
    print(f"Wybrane przedmioty: {wybrane}")
