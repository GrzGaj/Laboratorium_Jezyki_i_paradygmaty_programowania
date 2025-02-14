open System

let removeDuplicates words =
    words |> Set.ofList |> Set.toList

[<EntryPoint>]
let main argv =
    printf "Podaj słowa oddzielone spacjami: "
    let input = Console.ReadLine()
    match input with
    | null | "" -> printfn "Nie podano żadnych słów."
    | _ ->
        let words = input.Split(' ') |> Array.toList
        let uniqueWords = removeDuplicates words
        printfn "Unikalne słowa: %A" uniqueWords
    0
