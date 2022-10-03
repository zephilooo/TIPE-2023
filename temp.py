# n = -321392183912
#
# st = "hello world"
# print(' '.join(format(ord(x), 'b') for x in st))
# st = "hello world"
# print(' '.join(map(bin,bytearray(st,'utf8'))))
# print(n.bit_length())


omega = 5
def hachage(x):
    return hash(x) % omega

def creer_dict():
    return [[] for i in range(omega)]

def presente(D,k):
    i = hachage(k)
    for (k2,e) in D[i]:
        if k2==k:
            return True
    return False

def element(D,k):
    i = hachage(k)
    for (k2,e) in D[i]:
        if k2==k:
            return e

def ajout(D,k,e):
    D[hachage(k)].append((k,e))

def suppression(D,k):
    i = hachage(k)
    for j in range(len(D[i])): #D[i] = [(k1,e1),(k2,e2),(k3,e3),...,(kn,en)]
        if j[0]==k:
            return D[i][:j] + D[i][j+1:]


def modification(D,k,e):
    """ modifie l'élément associé à une clé, supposée présente """
    i = hachage(k)
    for j in range(len(D[i])): #D[i] = [(k1,e1),(k2,e2),(k3,e3),...,(kn,en)]
        if j[0]==k:
            return D[i][:j] + [(k,e)] + D[i][j+1:]


import random

class Maillon:

	def __init__(self, valeur, suivant=None):
		self.valeur = valeur
		self.suivant = suivant


class Pile:

	def __init__(self):
		self.taille = 0 # nombre d'assiettes dans la pile
		self.sommet = None


	def empiler(self, valeur):
		self.sommet = Maillon(valeur, self.sommet)
		self.taille += 1

	def depiler(self):
		if self.taille > 0:
			valeur = self.sommet.valeur
			self.sommet = self.sommet.suivant
			self.taille -= 1
			return valeur

	def estVide(self):
		return self.taille == 0


	def lireSommet(self):
		return self.sommet.valeur



def profondeur(G,s) :
    parcours = {s: None}
    queue = Pile()
    queue.empiler(s)
    while not(queue.estVide()) :
        u = queue.lireSommet()
        dejavu=[y for y in G[u] if y not in parcours]
        if dejavu != []: #Pour flex on pourrait même mettre if dejavu:
            v=random.choice(dejavu)
            parcours[v]=u
            queue.empiler(v)
        else :
            queue.depiler()
    return parcours

g_ex = {0 : [1], 1 : [4, 5], 2 : [0 , 3], 3 : [1, 7], 4 : [0], 5 : [7] , 6 : [3], 7 : [6, 8], 8 : [5]}

print(profondeur(g_ex,0))
