class Cell:
    def __init__(self, value):
        self.val = value
        self.next: Cell = None
    
    def __repr__(self):
        return "【"+str(self.val)+"】"
    
    
class Liste:
    def __init__(self):
        self.head: Cell = None
    
    def __repr__(self):
        s = "["
        c = self.head
        while c is not None:
            s += str(c)
            if c.next is not None:
                s+="🡒"
            c = c.next
        return s+"]"
    
    def copy(self):
        """
        Fait une copie d'une liste L, qui partage les mêmes cases.
        Faire des add ou des pop sur la copie n'affecte pas L,
        mais des insertSorted ou des remove si.
        """
        L = Liste()
        L.head = self.head
        return L
    
    def fullcopy(self):
        """
        Fait une copie d'une liste L, en créant de nouvelles cases.
        Aucune modification de la copie n'affecte L.
        """
        if self.head is None:
            return Liste()
        c = self.head
        endCell = Cell(c.val)
        L = Liste()
        L.head = endCell
        while c.next is not None:
            endCell.next = Cell(c.next.val)
            endCell = endCell.next
            c = c.next
        return L
    
    def add(self,v):
        """
        Ajoute une cellule contenant la valeur v en tête de liste
        Input :
            - L, une liste chaînée
            - v, une valeur
        La fonction doit créer la cellule contenant la valeur v et l'ajouter en tête de liste.
        """
        c = Cell(v)
        c.next = self.head
        self.head = c
    
    def pop(self):
        """
        Supprime la cellule en tête de liste
        Input : L, une liste chaînée
        Output : la valeur de la cellule supprimée. Si la liste est vide, on renvoie None et on ne fait rien.
        """
        if self.head is None:
            return None
        v = self.head.val
        self.head = self.head.next
        return v
    
    def remove(self,v):
        """
        Supprime la premiere occurence de v dans L
        Input :
            - L, une liste chaînée
            - v, une valeur
        Output : True si une valeur a été supprimée et False sinon
        """
        c = self.head
        if c is None:
            return False
        if c.val == v:
            self.pop()
            return True
        while c.next is not None:
            if c.next.val == v:
                c.next = c.next.next
                return True
            c = c.next
        return False
            
    def insertSorted(self,v):
        """
        Ajoute une cellule contenant la valeur v dans une liste triée, en maintenant le tri.
        Input :
            - L, une liste chaînée dont les valeurs sont triées par ordre croissant
            - v, une valeur
        La fonction doit créer la cellule contenant la valeur v et l'ajouter à la bonne position dans L.
        """
        c = self.head
        if c is None:
            self.add(v)
            return
        while c.next is not None and c.next.val < v:
            c = c.next
        cv = Cell(v)
        cv.next = c.next
        c.next=cv

def toListe(l):
    """
    Transforme une liste classique Python en lîste chaînée
    Input :
        - une liste Python (structure de tableau dynamique)
    Output: la liste chaînée correspondante
    """
    L = Liste()
    for i in range(len(l)-1,-1,-1):
        L.add(l[i])
    return L
'''
def fusion(L1,L2):
    """
    Fait l'union de deux listes chaînées triées
    Input :
        - L1,L2 : deux listes chaînées triées
    Output: la liste chaînée triée contenant l'union des valeurs de L1 et L2 (avec répétitions)
    """
    c1 = L1.head
    c2 = L2.head
    if c1 is None:
        return L2.copy()
    if c2 is None:
        return L1.copy()
    if c1.val < c2.val:
        L1 = L1.copy()
        L1.pop()
        L = fusion(L1,L2)
        L.add(c1.val)
        return L
    else:
        L2 = L2.copy()
        L2.pop()
        L = fusion(L1,L2)
        L.add(c2.val)
        return L
'''
    
def fusion(L1,L2):
    """
    Fait l'union de deux listes chaînées triées
    Input :
        - L1,L2 : deux listes chaînées triées
    Output: la liste chaînée triée contenant l'union des valeurs de L1 et L2 (avec répétitions)
    """
    c1 = L1.head
    c2 = L2.head
    L = Liste()
    endCell = None
    while c1 is not None or c2 is not None:
        if c2 is None or (c1 is not None and c1.val < c2.val):
           newCell = Cell(c1.val)
           c1 = c1.next
        else:
           newCell = Cell(c2.val)
           c2 = c2.next
        if endCell is None:
            L.head = newCell
        else:
            endCell.next = newCell
        endCell = newCell
    return L
  
'''  
def division(L):
    """
    Découpe une liste chaînée en deux listes chaînées de tailles presque égales.
    Input :
        - L : liste chaînée
    Output:
        - L1,L2 : deux listes chaînées telles que leur union contient les mêmes éléments que L,
                  et | |L1| - |L2| | ≤ 1
    """
    if L.head is None:
        return Liste(),Liste()
    v = L.pop()
    L1,L2 = division(L)
    L2.add(v)
    return L2,L1'''

def division(L):
    L1 = Liste()
    L2 = Liste()
    c1 = L.head
    if c1 is None:
        return L1,L2
    c2 = c1.next
    L1.add(c1.val)
    if c2 is None:
        return L1,L2
    L2.add(c2.val)
    while c2.next:
        c1 = c2.next
        c2 = c1.next
        L1.add(c1.val)
        if c2 is None:
            return L1,L2
        L2.add(c2.val)
    return L1,L2

def sort(L):
    if L.head is None or L.head.next is None:
        return L.fullcopy()
    L1,L2 = division(L.copy())
    return fusion(sort(L1),sort(L2))


#############################
# Fonctions de vérification #
#############################

def isSorted(L):
    ''' Vérifie qu'une liste chaînée est triée'''
    c = L.head
    if c is None:
        return True
    while c.next is not None:
        if c.next.val < c.val:
            return False
        c = c.next
    return True

"""
Les instructions de test.
Elles ne sont pas exécutées si on charge le fichier comme une librairie externe.
"""
if __name__ == '__main__':
    from utilities import shuffle, rapidityTest
        

    
    #########
    # Tests #
    #########
    
    LTest = Liste()
    LTest.add(3)
    LTest.add(2)
    LTest.add(1)
    assert str(LTest)=="[【1】🡒【2】🡒【3】]"
    
    L2 = LTest.copy()   
    assert L2.pop()==1
    assert L2.pop()==2
    assert L2.pop()==3
    assert L2.pop() is None
    assert str(L2)=="[]"
    
    L3 = toListe(range(1,10))
    assert L3.remove(3)
    assert not L3.remove(3)
    assert L3.remove(1)
    L3.insertSorted(4)
    L3.insertSorted(20)
    assert str(L3) == "[【2】🡒【4】🡒【4】🡒【5】🡒【6】🡒【7】🡒【8】🡒【9】🡒【20】]"
    
    L4 = fusion(LTest,L3)
    assert str(L4) == "[【1】🡒【2】🡒【2】🡒【3】🡒【4】🡒【4】🡒【5】🡒【6】🡒【7】🡒【8】🡒【9】🡒【20】]"
    
            
    t = list(range(10))
    shuffle(t)
    L5 = toListe(t)
    assert str(sort(L5)) == "[【0】🡒【1】🡒【2】🡒【3】🡒【4】🡒【5】🡒【6】🡒【7】🡒【8】🡒【9】]"
    
    # Test d'efficacité de insertSorted
    n = 10000
    t = list(range(n))
    shuffle(t)
    L6 = Liste()
    print("Création d'une liste triée de taille",n,":")
    time1 = rapidityTest(L6.insertSorted, t)
    assert isSorted(L6)
    
    # Test d'efficacité de sort
    L7 = toListe(t)
    print("\nTri d'une liste chaînée de taille",n,":")
    time2 = rapidityTest(sort,[L7])
    
    print("\nSur une liste chaînée de taille",n,"le tri fusion est",end=' ')
    print(int(time1/time2),"fois plus rapide que le tri par insertion.")
    