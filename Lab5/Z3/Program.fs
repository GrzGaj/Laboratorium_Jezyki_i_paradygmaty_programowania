//Zadanie 3 

let nums = [1; 2; 3]
let rec permutations lst =
    match lst with
    | [] -> [[]]  
    | x :: xs -> 
        let perms = permutations xs
        [ for perm in perms do
            for i in 0 .. List.length perm do
                yield List.insertAt i x perm ]

let result = permutations nums
printfn "%A" result