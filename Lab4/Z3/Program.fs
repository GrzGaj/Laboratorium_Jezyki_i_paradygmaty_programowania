open System
open System.Text.RegularExpressions

let countWords (text: string) =
    let words = Regex.Matches(text.ToLower(), "\w+") |> Seq.cast<Match> |> Seq.map (fun m -> m.Value)
    words |> Seq.length

let countCharsWithoutSpaces (text: string) =
    text |> Seq.filter (fun c -> not (Char.IsWhiteSpace c)) |> Seq.length

let mostFrequentWord (text: string) =
    let words = Regex.Matches(text.ToLower(), "\w+") |> Seq.cast<Match> |> Seq.map (fun m -> m.Value)
    let wordCounts = words |> Seq.groupBy id |> Seq.map (fun (w, instances) -> w, Seq.length instances)
    wordCounts |> Seq.maxBy snd

[<EntryPoint>]
let main argv =
    printf "Podaj tekst do analizy: "
    let inputText = Console.ReadLine()
    
    let wordCount = countWords inputText
    let charCount = countCharsWithoutSpaces inputText
    let (mostFreqWord, freq) = mostFrequentWord inputText
    
    printfn "Liczba słów: %d" wordCount
    printfn "Liczba znaków (bez spacji): %d" charCount
    printfn "Najczęściej występujące słowo: '%s' (wystąpienia: %d)" mostFreqWord freq
    
    0
