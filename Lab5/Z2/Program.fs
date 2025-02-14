// Zadanie 2 

//definicja wykorzystywanego typu
type BinarTree<'T>=
    | Empty
    | Node of 'T * BinarTree<'T> * BinarTree<'T>
//struktura drzewa
let tree = Node(10, 
            Node(5,
                Node(1, Empty, Empty),
                Node(18,Empty,Empty)
            ),
            Node(5,
                Node(51, Empty, Empty),
                Node(3,Empty,Empty)
            )
            )
//wyszukiwanie rekurencyjne
let rec szukajRec tree value =
    match tree with
    | Empty -> false
    | Node (v, left, right) ->
        if v = value then true
        else szukajRec left value || szukajRec right value
//wyszukiwanie iteracyjne
let szukajItr tree value =
    let rec iter stack =
        match stack with
        | [] -> false
        | Empty :: rest -> iter rest
        | Node (v, left, right) :: rest ->
            if v = value then true
            else iter (right :: left :: rest)
    
    iter [tree]


let wynikRec = szukajRec tree 21   
let wynikItr = szukajItr tree 5

printfn "Wynik wyszukiwania rekurencyjnego %b" wynikRec
printfn "Wynik wyszukiwania iteracyjnego %b" wynikItr
