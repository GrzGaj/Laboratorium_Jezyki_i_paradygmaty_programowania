// For more information see https://aka.ms/fsharp-console-apps
open System

//rekord user
type User = {
Weight:float
Height:float
}

//funkcja do obliczania BMI
let calculateBMI(user: User) =
    let heightMeters = user.Height / 100.00
    let bmi = user.Weight / (heightMeters ** 2.0)
    bmi


 //funkcje do określania kategorii
let getCategoryBMI bmi =
    match bmi with
    | x when x < 18.5 -> "Niedowaga"
    | x when x >= 18.5 && x < 24.99 -> "Niedowaga"
    | x when x >= 25.0 -> "Nadwaga"
    | _ -> "Otyłość"


[<EntryPoint>]
let main argv =
    printfn "Podaj wage w kg:"
    let weightInput = Console.ReadLine()
    printfn "Podaj wzrost:"
    let heightInput = Console.ReadLine()

    let weight = 
        match Double.TryParse(weightInput) with
        | (true, value) -> value
        |_ ->
            printfn "Nieprawidłowa waga"
            0.0

    let height = 
        match Double.TryParse(heightInput) with
        | (true, value) -> value
        |_ ->
            printfn "Nieprawidłowy wzrost"
            0.0

    if weight > 0 && height > 0 then
        let user = {Weight = weight; Height = height}
        let bmi = calculateBMI user
        let category = getCategoryBMI bmi
        printfn "Twoje BMI %.2f" bmi
        printfn "kategoria BMI: %s" category
        
    else
        printfn "nieprawidłowe dane wejściowe"

    0