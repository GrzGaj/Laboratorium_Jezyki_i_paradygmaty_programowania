// Rekurencyjna implementacja problemu Wież Hanoi
let rec hanoi n poczatek cel temp =
    if n > 0 then
        hanoi (n - 1) poczatek temp cel
        printfn "Przenieś dysk %d z %s do %s" n poczatek cel
        hanoi (n - 1) temp cel poczatek

// Iteracyjna implementacja problemu Wież Hanoi
let hanoi_iteracja n poczatek cel temp =
    let moves = pown 2 n - 1 
    let stacks = [|(List.init n (fun i -> n - i)); []; []|]
    let names = [|poczatek; temp; cel|]
    
    let przeun fromIdx toIdx =
        match stacks.[fromIdx] with
        | h :: t ->
            stacks.[fromIdx] <- t
            stacks.[toIdx] <- h :: stacks.[toIdx]
            printfn "Przenieś dysk %d z %s do %s" h names.[fromIdx] names.[toIdx]
        | [] -> ()
    
    for i in 1..moves do
        let fromIdx, toIdx =
            match n % 2 with
            | 0 -> [(0, 1); (0, 2); (1, 2)].[i % 3]
            | _ -> [(0, 2); (0, 1); (2, 1)].[i % 3]
        
        let (fromIdx, toIdx) =
            if stacks.[fromIdx] = [] || (stacks.[toIdx] <> [] && List.head stacks.[toIdx] < List.head stacks.[fromIdx]) then
                toIdx, fromIdx
            else
                fromIdx, toIdx
        
        przeun fromIdx toIdx

hanoi 3 "A" "C" "B"
hanoi_iteracja 3 "A" "C" "B"
