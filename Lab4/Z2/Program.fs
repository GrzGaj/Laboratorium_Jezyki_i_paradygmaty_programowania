open System

// Zdefiniowanie kursów wymiany w mapie, w tym PLN
let exchangeRates = 
    Map [
        ("USD", Map [("EUR", 0.93); ("GBP", 0.75); ("USD", 1.0); ("PLN", 4.45)])
        ("EUR", Map [("USD", 1.08); ("GBP", 0.81); ("EUR", 1.0); ("PLN", 4.78)])
        ("GBP", Map [("USD", 1.33); ("EUR", 1.24); ("GBP", 1.0); ("PLN", 5.88)])
        ("PLN", Map [("USD", 0.22); ("EUR", 0.21); ("GBP", 0.17); ("PLN", 1.0)])
    ]

// Funkcja przeliczająca walutę
let convertCurrency (amount: float) (sourceCurrency: string) (targetCurrency: string) =
    if exchangeRates.ContainsKey(sourceCurrency) then
        let rates = exchangeRates.[sourceCurrency]
        if rates.ContainsKey(targetCurrency) then
            let rate = rates.[targetCurrency]
            amount * rate
        else
            printfn "Nie obsługujemy konwersji z %s na %s." sourceCurrency targetCurrency
            0.0
    else
        printfn "Nie obsługujemy waluty %s." sourceCurrency
        0.0

// Funkcja obsługująca dane wejściowe od użytkownika
let getUserInput() =
    printfn "Podaj kwotę do przeliczenia:"
    let amount = Console.ReadLine() |> float
    printfn "Podaj walutę źródłową (np. USD, EUR, GBP, PLN):"
    let sourceCurrency = Console.ReadLine().ToUpper()
    printfn "Podaj walutę docelową (np. USD, EUR, GBP, PLN):"
    let targetCurrency = Console.ReadLine().ToUpper()
    amount, sourceCurrency, targetCurrency

// Główna funkcja programu
let main() =
    let amount, sourceCurrency, targetCurrency = getUserInput()
    let convertedAmount = convertCurrency amount sourceCurrency targetCurrency
    if convertedAmount > 0.0 then
        printfn "Przeliczona kwota: %.2f %s" convertedAmount targetCurrency

// Uruchomienie programu
main()
