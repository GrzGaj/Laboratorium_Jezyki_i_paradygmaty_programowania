open System

let isPalindrome (input: string) =
    let cleaned = input.ToLower().Replace(" ", "")
    cleaned = String(cleaned.ToCharArray() |> Array.rev)

[<EntryPoint>]
let main argv =
    printf "Podaj ciąg znaków: "
    let userInput = Console.ReadLine()
    if isPalindrome userInput then
        printfn "Podany ciąg jest palindromem."
    else
        printfn "Podany ciąg nie jest palindromem."
    0