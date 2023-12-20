let board = [[0; 0; 4;  8; 0; 0;  0; 1; 7];
             [6; 7; 0;  9; 0; 0;  0; 0; 0];
             [5; 0; 8;  0; 3; 0;  0; 0; 4];
             [3; 0; 0;  7; 4; 0;  1; 0; 0];
             [0; 6; 9;  0; 0; 0;  7; 8; 0];
             [0; 0; 1;  0; 6; 9;  0; 0; 5];
             [1; 0; 0;  0; 8; 0;  3; 0; 6];
             [0; 0; 0;  0; 0; 6;  0; 9; 1];
             [2; 4; 0;  0; 0; 1;  5; 0; 0]];;

let board = [[8; 1; 0;  3; 0; 7;  0; 0; 6];
             [6; 0; 0;  0; 0; 0;  0; 0; 9];
             [0; 2; 5;  0; 0; 0;  0; 3; 4];
             [3; 0; 0;  9; 0; 0;  0; 7; 0];
             [0; 7; 0;  0; 8; 5;  0; 2; 0];
             [0; 0; 0;  1; 0; 0;  6; 0; 0];
             [0; 0; 0;  5; 0; 0;  0; 9; 7];
             [1; 0; 0;  0; 0; 0;  8; 0; 0];
             [0; 8; 4;  0; 6; 2;  0; 0; 0]];;

let rec sup e1 l2 = match l2 with []->[] |e::l when e = e1-> sup e1 l |e::l-> e:: sup e1 l;;
let rec is_possible list = let rec possible list1 list2 = match list1 with []-> list2 |e::l -> possible l (sup e list2)
  in let decimal = [1;2;3;4;5;6;7;8;9] in possible list decimal;;
let rec nth n board = match board with []-> failwith "nth"|e::l when n=0-> e |e::l-> nth (n-1) l;;
let rec get_row n board = let rec aux n board = match board with []-> failwith "get_row" |e::l when n=0 -> e |e::l-> aux (n-1) l in let n=(n/9) in aux n board;;
let rec get_col n board = match board with []->[] |e::l-> (nth (n mod 9) e) :: (get_col n l);;
let rec get_square n = match n with 1|2|3|10|11|12|19|20|21-> 11 |4|5|6|13|14|15|22|23|24-> 14 |7|8|9|16|17|18|25|26|27-> 17
                                  |28|29|30|37|38|39|46|47|48-> 38 |31|32|33|40|41|42|49|50|51-> 41 |34|35|36|43|44|45|52|53|54 -> 44
                                  |55|56|57|64|65|66|73|74|75-> 64 |58|59|60|67|68|69|76|77|78-> 68 |61|62|63|70|71|72|79|80|81-> 71 |n-> failwith "get_square";;
let rec convert n = let n =(n-1) in (n/9,n mod 9);;
let rec get_neighbours n board = let n = (get_square n) in let (x,y) = convert n in
  let rec count (a,b) board = match board with
    |[] -> []
    |e_ligne::l_ligne-> ( let rec count_colonne (a,b) board = match board with
          [] -> count (a+1,0) l_ligne
        |e_col::l_col-> (match a with
              f when f = (x-1) || f = x || f = (x+1) -> (match b with
                |g when (g = (y-1) && e_col <> 0)|| (g = y && e_col <> 0)|| (g = (y+1) && e_col <> 0) ->  e_col :: count_colonne (a,b+1) l_col
                |_-> count_colonne (a,b+1) l_col)
            |_-> count (a+1,0) l_ligne) in count_colonne (a,b) e_ligne )
  in count (0,0) board ;;
let rec present x list = match list with []-> false |e::l when e =x -> true |e::l-> present x l;;
let rec merge list1 list2 list3 = let rec aux list check = match list with []-> []
                                                                         |e::l when present e check || e = 0 -> aux l check
                                                                         |e::l-> e::(aux l (e::check))
  in aux (list1@list2@list3) [];;
let rec put_cell v (x ,y) board = let rec colonne v y board =
                                    match y with
                                      0-> (match board with []->[] |e::l-> v::l)
                                    |_ -> (match board with []->[] |e::l->
                                        e ::(colonne v (y-1) l))in
  match x with
    0-> (match board with []->[] |e::l-> (colonne v y e) :: l)
  |_ -> ( match board with []->[] |e::l-> e :: (put_cell v ((x-1), y) l)) ;;
let rec get_cell  (x ,y) board = let rec colonne y board =
                                   match y with
                                     0-> (match board with []->0 |e::l -> e)
                                   |_ -> (match board with [] ->0 |e::l -> colonne (y-1) l )
  in  match x with
    0-> (match board with []->0 |e::l-> colonne y e)
  |_ ->(match board with []->0 |e::l -> get_cell ((x-1), y) l);;
let rec sudoku board = let rec solve n board = match n with
      n when n = 82|| n > 82-> board
    |n-> (match get_cell (convert n) board with g when g =0 ->( match is_possible (merge (get_row (n-1) board)(get_col (n-1) board)(get_neighbours (n) board)) with
          []-> solve (n+1) board
        |e::[]-> solve (1) (put_cell e (convert n) board)
        |e::l-> solve (n+1) board)
                                              |g-> solve (n+1) board) in solve 1 board;;
sudoku board;;
