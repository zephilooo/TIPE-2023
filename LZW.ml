type dictionnaire_arbre = V | N of char*bool*int*dictionnaire_arbre*dictionnaire_arbre;;

(*bool vaut True si le caractère termine le mot, int est la valeur sur laquelle la suite de caractère est codée (si le caractère termine un mot, 
int vaut la valeur du mot dans le dictionnaire LZW, sinon -1)*)

let hash str_list = 0;;

let rec string_to_list str = let res = ref [] and n = String.length str in
  for i = n-1 downto 0 do
    res := str.[i]::!res
  done;!res;;


let ajoute str a = let liste_str = string_to_list str in (* Ajoute un mot dans le dictionnaire*)
  let rec aux a l = match a,l with
    |_,[] -> failwith "Liste de caractere vide"
    |V,t::q -> if q = [] then N(t,true,hash l,V,V) else N(t,false,-1,V,aux V q)
    |N(cara,booleen,code,g,d),t::q -> if cara=t then N(cara,booleen,code,g,aux d q)
        else if q = [] then N(cara,booleen,code,N(t,true,hash l,V,V),d) else N(cara,booleen,code,N(t,false,-1,V,aux V q),d)
  in aux a liste_str;;


let arb2 = ajoute "mo" V;;
let arbr3 = ajoute "mot" arb2;;

let est_present str arbre = let liste_str = string_to_list str in (*Détermine si un mot est présent dans le dictionnaire*) 
  let rec aux a l = match a,l with
    |_,[] -> failwith "Liste de caractère vide"
    |V,_ -> false 
    |N(cara,booleen,code,g,d),[elem] -> (cara = elem && booleen) || aux g [elem]
    |N(cara,booleen,code,g,d),t::q when t=cara -> aux d q
    |N(cara,booleen,code,g,d),t::q -> aux g (t::q)
  in aux arbre liste_str;;

est_present "mo" arbr3;;
est_present "mote" arbr3;;