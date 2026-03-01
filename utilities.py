from time import process_time as pt
from math import sqrt
from random import randint

def progress_bar(current, total, width=40):
    ''' Affiche une frame d'une barre de progression.
    '''
    filled = int(current * width / total)
    bar = "█" * filled + "-" * (width - filled)
    #\r déplace le curseur au début de la ligne en cours d'écriture
    print(f"\r|{bar}| {current*100//total}%",sep='',end='')
    
def rapidityTest(f, args):
    ''' Applique la fonction f tour à tour sur chaque élément d'un tableau args.
        Affiche une barre de progression au cours de ces exécutions.
        Affiche et retourne le temps de calcul total.
    '''
    n = len(args)
    nsteps = 100
    step = max(1,(n-1)//nsteps)
    t0 = pt()
    print(" Calcul en cours...")
    for i,x in enumerate(args):
        if i % step == (n-1) % step:
            progress_bar(i,n)
        if isinstance(x,(tuple,list)):
            f(*x)
        else:
            f(x)
    progress_bar(n,n)
    tf = pt()
    print("\n\nCalcul terminé en",tf-t0,"secondes.")
    return tf-t0
    

def shuffle(t):
    ''' Mélange uniformément les valeurs d'un tableau t
    '''
    for i in range(len(t)-1):
        j = randint(i,len(t)-1)
        t[i],t[j] = t[j],t[i]
        

if __name__=='__main__':
    # Example d'utilisation de rapidityTest
    def add(x,y):
        return x+y
    def mult(x,y):
        return x*y
    
    n = 2000000
    args = [(i,i) for i in range(n)]
    print("Calcul de",n,"additions:")
    rapidityTest(add,args)
    print("\nCalcul de",n,"multiplications:")
    rapidityTest(mult,args)
    
    args = list(range(n))
    print("\nCalcul de",n,"racines carrées:")
    rapidityTest(sqrt,args)