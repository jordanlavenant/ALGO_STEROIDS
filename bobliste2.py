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
    # TODO
    return
    
def pop(L):
    ''' Supprime la première case de L
    Input: L, une Bobliste
    Output: La valeur de la première case de L si elle existe, None sinon. 
    '''
    # TODO
    return
    
def getElement(L,i):
    ''' Accès à la i-ème case de L
    Input: L, une Bobliste
    Output: La valeur de la case en position i dans L si elle existe, None sinon.
    '''
    # TODO
    return

def insertSorted(L,v):
    ''' Insertion de la valeur v dans une Bobliste triée
    Input: L, une Bobliste triée ; v, une valeur correspondant au type interne des cases de L
    Output: pas d'output ; on modifie L en place en insérant une case de valeur v
            au bon endroit pour qu'elle reste triée.
    '''
    # TODO
    return
    
def remove(L,v):
    ''' Suppression de la première case de valeur v dans une Bobliste triée
    Input: L, une Bobliste triée ; v, une valeur correspondant au type interne des cases de L
    Output: True si une case de valeur v a été trouvée puis supprimée, False sinon (L reste inchangée)
    '''
    # TODO
    return

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