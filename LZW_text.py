import random as rd
from math import log
import pickle
import struct

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
    """ Indique le nombre de bits nécessaires à l'encodage du texte dans sa forme brute"""
    dico = {chr(i): i for i in range(256)}
    n = len(texte)
    if n<10000:
        print("Le texte originel était le suivant : " + '\n'+ texte )
    print("En supposant que chaque caractère est codé sur 8 bits (1 octet), le texte nécessite {} bits, soit {} Ko pour être encodé".format(8*n,n/1000))


def afficher_compressed_bin(liste):
    """ Indique le nombre de bits nécessaires à l'encodage du texte dans sa forme compressée"""
    n = len(liste)
    print(n)
    m = max(liste)
    bits_max = int(log(m)/log(2)) +1
    p=bits_max*n
    print("La transformation LZW permet de réduire le nombre de bits nécessaires à l'écriture du texte à {} bits, soit {} Ko \n".format(p,2*n/1000))
    print("Remarque : la longueur du dictionnaire qui a été généré pour encoder le texte est de {}".format(n))

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


def ecrire_code_bin(liste):
    with open('compressed_maison_pack.bin','wb') as file:
        for i in liste:
            file.write(struct.pack("i", i))

    with open('compressed_maison_pickle.bin','wb') as file:
        pickle.dump(liste,file)

    # with open('test.txt', 'wb') as file:
    #     for elem in liste:
    #         #print(chr(elem).encode('utf-16'))
    #         file.write(chr(elem).encode('utf-16'))

def main(texte):
    c = compresse(texte)
    code_bin = [bin(n) for n in c]

    afficher(texte)
    ecrire_code_bin(c)
    afficher_compressed_bin(c)

    #print(decompresse(c))

texte = recup_text("tocompress.txt")

main(texte)
