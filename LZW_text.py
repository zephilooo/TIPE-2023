import random as rd
from math import log
# def make_dict(n):
#     d = {i: chr(i) for i in range(256)}
#     for i in range(256,256+n):
#         d[i] = ""
#     return d
#
# def dernier_vide(dict):
#     for k,v in dict.items():
#         if v == "":
#             return k                              ------->>>>>>> AMELIORATION POSSIBLE AVEC UNE TAILLE FIXE?
#     return -1
#
# dict = make_dict(7)
# values = list(dict.values())
#
# def index(dict,s):
#     return dict.index(s)


# def write_text(texte):
#     file = open("temp.txt","w")
#     for elem in texte:
#         file.write(elem)


def afficher(texte):
    dico = {chr(i): i for i in range(256)}
    n = len(texte)
    if n<10000:
        print("Le texte originel était le suivant : " + '\n'+ texte )
    print("En supposant que chaque caractère est codé sur 8 bits (1 octet), le texte nécessite {} bits, soit {} octets pour être encodé".format(8*n,n))


def afficher_compressed_bin(liste):
    "On suppose que l'entier maximal est inférieur à 65536"
    n = len(liste)
    m = max(liste)
    bits_max = int(log(m)/log(2)) +1
    p=bits_max*n
    print("La transformation LZW permet de réduire le nombre de bits nécessaires à l'écriture du texte à {} bits, soit {} octets".format(p,2*n))

def compresse(chaine):
    "Prend en entrée une chaine de caractère et renvoie une liste dont les élements sont les valeurs codées en entiers décimaux permettant de compresser la chaîne"
    dico_size = 256
    dico = {chr(i): i for i in range(dico_size)}

    res = []
    sequence = ""

    for caractereCourant in chaine:
        sequenceCourante = sequence + caractereCourant
        if sequenceCourante in dico:
            sequence = sequenceCourante
        else:
            # print(sequence)
            res.append(dico[sequence])
            dico[sequenceCourante] = dico_size
            sequence = caractereCourant
            dico_size += 1

    res.append(dico[sequence])
    return res

def decompresse(compressed):
    """Décompresse une liste d'entiers en chaîne de caractères"""
    from io import StringIO

    dict_size = 256
    dico = {i: chr(i) for i in range(dict_size)}

    # on utilise StringIO, sinon ça devient un  O(N^2), à cause d'une concaténation de string dans la boucle
    result = StringIO()
    sequence = chr(compressed.pop(0))
    result.write(sequence)

    for k in compressed:
        if k in dico:
            entree = dico[k]
        elif k == dict_size:
            entree = sequence + sequence[0]
        else:
            raise ValueError("Problème de décompression")
        result.write(entree)
        # print(entree)

        dico[dict_size] = sequence + entree[0]
        dict_size += 1

        sequence = entree
    return result.getvalue()


def recup_text(namefile):
    with open(namefile,'r',encoding='utf-8') as f:
        res = f.readlines()
    txt = ""
    for ligne in res:
        txt += ligne
    return txt

texte = recup_text("tocompress.txt")
print(texte)

def affichage_style(texte):
    i = 0
    print('SYSencrypt')
    dico = {i: chr(i) for i in range(256)}
    while i<500000:
        if i*2==500000:
            j=0
            while j< 500000:
                print('',end='-')
                j+= 1
        if i%1000==0:
            print('SYSencrypt')
        i+=1
        print(dico[rd.randint(41,125)],end="")

    print('\n\n\n')
    c = compresse(texte)
    afficher_compressed_bin(c)
    afficher(texte)
    print(decompresse(c))

affichage_style(texte)
