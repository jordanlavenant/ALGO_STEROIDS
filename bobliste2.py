from liste import Cell, isSorted
from math import isqrt

class Cell2:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return "【"+str(self.val)+"】"

class Bobliste:
    def __init__(self, v=None):
        self.head = Cell(v) if v else None
        self.bobhead = Cell2(v) if v else None
        self.n = 1 if v else 0
    
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
                s+="⟷"
            c = c.next
        return s+"\n"

def add(L,v):
    ''' Ajoute une case au début de L
    Input: L, une Bobliste
    Output: pas d'output ; on ajoute en place une case de valeur v en tête de L
    '''
    new_cell = Cell2(v)
    # Insertion dans la liste principale & incrémentation de la taille
    if L.head is not None:
        L.head.prev = new_cell # Mise à jour du pointeur "prev" de l'ancienne tête
        new_cell.next = L.head # Mise à jour du pointeur "next" de la nouvelle tête

    L.head = new_cell
    L.n += 1

    # Si la nouvelle longueur de L est un carré parfait, on ajoute une nouvelle bobcell
    if isqrt(L.n) ** 2 == L.n:
        new_bobcell = Cell2(new_cell) # Nouveau bobcell, avec le pointeur vers la cell standart
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
    L.head.prev = None # Mise à jour du pointeur "prev" de la nouvelle tête
    L.n -= 1

    # Mise à jour de la liste secondaire
    if L.bobhead is not None and L.bobhead.val == cell:
        L.bobhead = L.bobhead.next # Prochaine bobcase ou "None" si elle n'existe pas
        L.bobhead.prev = None # Mise à jour du pointeur "prev" de la nouvelle tête de bobliste

    return cell
    
def getElement(L,i):
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
    # Liste vide ou insertion en tête
    if L.head is None or v <= L.head.val:
        add(L, v)
        return

    best_cell = L.head

    bob = L.bobhead
    # k est le compteur décrémental du parcours de la liste secondaire (initialiser au bobhead)
    k = isqrt(L.n)

    while bob is not None and k >= 1:
        # Si la valeur de la bobcase est inférieure à v, on continue à parcourir
        if bob.val.val < v:
            best_cell = bob.val
            bob = bob.next
            # Prochain indice
            k -= 1
        else:
            break

    prev = best_cell
    current = best_cell.next

    while current is not None:
        # Si la valeur de la bobcase est inférieure à v, on continue à parcourir
        if current.val < v:
            prev = current
            current = current.next
        else:
            break

    # Insertion de la nouvelle case
    new_cell = Cell(v)
    new_cell.next = current
    new_cell.prev = prev
    prev.next = new_cell
    if current:
        current.prev = new_cell
    L.n += 1

    # Mise à jour de la bobliste
    k_prec = isqrt(L.n - 1)
    k_new = isqrt(L.n)

    # Si k_new > k_prec, on ajoute une nouvelle bobcase en tête
    if k_new > k_prec:
        new_bobcell = Cell(L.head)
        new_bobcell.next = L.bobhead
        L.bobhead = new_bobcell

    bob = L.bobhead

    # Sauter la nouvelle bobcase déjà correcte
    if k_new > k_prec:
        bob = bob.next

    while bob is not None:
        # Décalage vers la case suivante pour les bobcases pointant les cases ayant une valeur inférieure à la v insérée
        if bob.val.val < v:
            bob.val = bob.val.next
        bob = bob.next
    
def remove(L,v):
    ''' Suppression de la première case de valeur v dans une Bobliste triée
    Input: L, une Bobliste triée ; v, une valeur correspondant au type interne des cases de L
    Output: True si une case de valeur v a été trouvée puis supprimée, False sinon (L reste inchangée)
    '''
    # Liste vide
    if L.head is None:
        return False

    # Suppression de la tête si elle a la valeur v
    if L.head.val == v:
        pop(L)

        # Mise à jour de la bobliste
        k_prec = isqrt(L.n + 1)
        k_new = isqrt(L.n)

        if k_new < k_prec:
            L.bobhead = L.bobhead.next
            if L.bobhead:
                L.bobhead.prev = None

        return True

    # Recherche de la case à supprimer
    best_cell = L.head

    bob = L.bobhead
    # k est le compteur décrémental du parcours de la liste secondaire (initialiser au bobhead)
    k = isqrt(L.n)

    while bob is not None and k >= 1:
        # Si la valeur de la bobcase est inférieure à v, on continue à parcourir
        if bob.val.val < v:
            best_cell = bob.val
            bob = bob.next
            # Prochain indice
            k -= 1
        else:
            break

    prev = best_cell
    current = best_cell.next

    while current is not None:
        # Si la valeur de la bobcase est inférieure à v, on continue à parcourir
        if current.val < v:
            prev = current
            current = current.next
        else:
            break
    
    # Suppression de la case de valeur v si elle existe
    if current is not None and current.val == v:
        prev.next = current.next
        if current.next:
            current.next.prev = prev
        L.n -= 1

        # Mise à jour de la bobliste
        k_prec = isqrt(L.n + 1)
        k_new = isqrt(L.n)

        # Si k_new < k_prec, on supprime la bobcase en tête
        if k_new < k_prec:
            L.bobhead = L.bobhead.next
            if L.bobhead:
                L.bobhead.prev = None

        bob = L.bobhead

        while bob is not None:
            # Décalage vers la case précédente pour les bobcases pointant les cases ayant une valeur inférieure à la v supprimée
            if bob.val.val < v:
                bob.val = bob.val.prev
            bob = bob.next
        
        return True
    return False


#############################
# Fonctions de vérification #
#############################

def check(L):
    ''' Vérifie qu'une liste doublement chaînée est cohérente'''
    c = L.head
    if c is None:
        return True
    if c.prev is not None:
        return False
    while c.next:
        if c.next.prev is not c:
            return False
        c = c.next
    return True

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
        text += "head 🡒【0】⟷【1】⟷【2】⟷【3】⟷【4】⟷【5】⟷【6】⟷【7】⟷【8】⟷【9】⟷【10】"
        text += "⟷【11】⟷【12】⟷【13】⟷【14】⟷【15】⟷【16】⟷【17】⟷【18】⟷【19】\n"
        assert str(L) == text
        assert check(L)
        for i in range(20):
            assert getElement(L,i)==i
        print("Le test de validité pour add et getElement est un succès!\n")
    
    # Test de rapidité pour add et getElement
    def test2():
        ''' Construit une bobliste de taille 100000.
            Mesure le temps de construction.
            Mesure le temps d'accès aux éléments.
        '''
        n = 100000
        L = Bobliste()
        args = [(L,i) for i in range(n-1,-1,-1)]
        print("Construction d'une bobliste de taille",n,":")
        assert rapidityTest(add,args) < 1
        args = [(L,i) for i in range(n)]
        print("\nAccès aux éléments de la bobliste :")
        assert rapidityTest(getElement,args) < 10
        print("Le test de rapidité pour add et getElement est un succès!\n")
        
    # Test de validité pour insertSorted et remove
    def test3():
        L = toBobliste(range(1,10))
        assert remove(L,3)
        assert not remove(L,3)
        assert remove(L,1)
        insertSorted(L,4)
        insertSorted(L,20)
        text = "bobhead 🡒【【2】】🡒【【7】】🡒【【20】】\n"
        text += "head 🡒【2】⟷【4】⟷【4】⟷【5】⟷【6】⟷【7】⟷【8】⟷【9】⟷【20】\n"
        assert str(L) == text
        print("Le test de validité pour insertSorted et remove est un succès!\n")
        
    # Test de rapidité pour insertSorted
    def test4():
        n = 10000
        t = list(range(n))
        shuffle(t)
        L = Bobliste()
        args = [(L,x) for x in t]
        print("Création d'une liste triée de taille",n,":")
        assert rapidityTest(insertSorted, args) < 1
        print("Le test de rapidité pour insertSorted est un succès!\n")
    
    # Test de rapidité pour remove
    def test5():
        n = 10000
        L = toBobliste(range(n))
        args = list(range(n))
        shuffle(args)
        def rm(x):
            assert remove(L,x)
        assert rapidityTest(rm,args) < 1
        print("Le test de rapidité pour remove est un succès!\n")

    # Exécution des tests (vous pouvez commenter ceux qui concernent une partie pas encore implémentée)
    test1()
    test2()
    test3()
    test4()
    test5()