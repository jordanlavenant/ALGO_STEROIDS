from liste import Cell, isSorted
from math import isqrt

class Bobliste:
    def __init__(self):
        self.head = None
        self.bobhead = None
        self.n = 0
    
    def __repr__(self):
        s = "bobhead 🡒"
        c = self.bobhead
        while c is not None:
            s += str(c)
            if c.next is not None:
                s+="🡒"
            c = c.next
        
        c = self.head
        s += "\nhead 🡒"
        while c is not None:
            s += str(c)
            if c.next is not None:
                s+="🡒"
            c = c.next
        return s+"\n"

#########################
# Fonctions à implanter #
#########################

def add(L,v):
    ''' Ajoute une case au début de L
    Input: L, une Bobliste
    Output: pas d'output ; on ajoute en place une case de valeur v en tête de L
    '''
    new_cell = Cell(v)
    # Insertion dans la liste principale & incrémentation de la taille
    if L.head is not None:
        new_cell.next = L.head
    L.head = new_cell
    L.n += 1

    # Si la nouvelle longueur de L est un carré parfait, on ajoute une nouvelle bobcell
    if isqrt(L.n) ** 2 == L.n:
        new_bobcell = Cell(new_cell) # Nouveau bobcell, avec le pointeur vers la cell standart
        new_bobcell.next = L.bobhead
        L.bobhead = new_bobcell

def pop(L):
    ''' Supprime la première case de L
    Input: L, une Bobliste
    Output: La valeur de la première case de L si elle existe, None sinon. 
    '''
    if L.head is None:
        return None

    cell = L.head
    # Mise à jour de la tête de la liste principale
    L.head = cell.next # Prochaine case ou "None" si elle n'existe pas
    L.n -= 1

    # Mise à jour de la liste secondaire
    if L.bobhead is not None and L.bobhead.val == cell:
        L.bobhead = L.bobhead.next # Prochaine bobcase ou "None" si elle n'existe pas

    return cell

def getElement(L, i):
    ''' Accès à la i-ème case de L
    Input: L, une Bobliste
    Output: La valeur de la case en position i dans L si elle existe, None sinon.
    '''
    if i < 0 or i >= L.n:
        return None

    best_cell = L.head
    best_index = 0

    bob = L.bobhead
    # k est le compteur décrémental du parcours de la liste secondaire (initialiser au bobhead)
    k = isqrt(L.n)

    while bob is not None and k >= 1:
        # Accès à la position i via le parcours de la bobliste
        curr_i = L.n - (k**2)

        # Si le curr_index est supérieur à i recherché, on s'arrête
        if curr_i > i:
            break

        best_cell = bob.val
        best_index = curr_i
        bob = bob.next
        # Prochain indice
        k -= 1

    current = best_cell
    for _ in range(i - best_index):
        current = current.next
    return current.val

def insertSorted(L,v):
    ''' Insertion de la valeur v dans une Bobliste triée
    Input: L, une Bobliste triée ; v, une valeur correspondant au type interne des cases de L
    Output: pas d'output ; on modifie L en place en insérant une case de valeur v
            au bon endroit pour qu'elle reste triée.
    '''
    # TODO
    return


#############################
# Fonctions de vérification #
#############################

def toBobliste(t):
    """ Transforme un tableau t (sous la forme d'une liste Python) en bobliste L
    """
    L = Bobliste()
    for i in range(len(t)-1,-1,-1):
        add(L,t[i])
    return L


if __name__ == '__main__':
    ''' Une série de tests permettant de vérifier votre code.
    Vous pouvez en ajouter si vous le désirez, à condition que cela soit dans ce bloc.
    Ainsi, ces tests ne sont pas exécutés si le fichier est importé comme une librairie externe.
    '''
    from utilities import shuffle, rapidityTest
    
    #####################    
    # Fonctions de test #
    #####################

    # Test de validité pour add et getElement
    def test1():
        ''' Construit une bobliste de taille 20 par insertions en tête successives.
            Vérifie que la bobliste obtenue est correcte.
            Vérifie que l'accès aux éléments est correct.
        '''
        L = toBobliste(range(20))
        text = "bobhead 🡒【【4】】🡒【【11】】🡒【【16】】🡒【【19】】\n"
        text += "head 🡒【0】🡒【1】🡒【2】🡒【3】🡒【4】🡒【5】🡒【6】🡒【7】🡒【8】🡒【9】🡒【10】"
        text += "🡒【11】🡒【12】🡒【13】🡒【14】🡒【15】🡒【16】🡒【17】🡒【18】🡒【19】\n"
        assert str(L) == text
        for i in range(20):
            assert getElement(L,i)==i
        print("Le test de validité pour add et getElement est un succès!\n")
    
    # Test de rapidité pour add et getElement
    def test2():
        ''' Construit une bobliste de taille 100000.
            Mesure le temps de construction.
            Mesure le temps d'accès aux éléments.
        '''
        n = 50000
        L = Bobliste()
        args = [(L,i) for i in range(n-1,-1,-1)]
        print("Construction d'une bobliste de taille",n,":")
        assert rapidityTest(add,args) < 0.5
        args = [(L,i) for i in range(n)]
        print("\nAccès aux éléments de la bobliste :")
        assert rapidityTest(getElement,args) < 5
        print("Le test de rapidité pour add et getElement est un succès!\n")
        
    # Test de validité pour insertSorted et remove
    def test3():
        L = toBobliste(range(1,10))
        insertSorted(L,4)
        insertSorted(L,20)
        text = "bobhead 🡒【【3】】🡒【【7】】🡒【【20】】\n"
        text += "head 🡒【1】🡒【2】🡒【3】🡒【4】🡒【4】🡒【5】🡒【6】🡒【7】🡒【8】🡒【9】🡒【20】\n"
        assert str(L) == text
        print("Le test de validité pour insertSorted et remove est un succès!\n")
        
    # Test de rapidité pour insertSorted
    def test4():
        n = 50000
        t = list(range(n))
        shuffle(t)
        L = Bobliste()
        args = [(L,x) for x in t]
        print("Création d'une liste triée de taille",n,":")
        assert rapidityTest(insertSorted, args) < 10
        print("Le test de rapidité pour insertSorted est un succès!\n")

    # Exécution des tests (vous pouvez commenter ceux qui concernent une partie pas encore implémentée)
    test1()
    test2()
    # test3()
    # test4()