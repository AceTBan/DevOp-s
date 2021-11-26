# Écrire une fonction f7 qui prend deux nombres en entrée et qui retourne le plus grand des deux.
a=22
b=5

def f7(a,b):
    if a>b:
        return a
    if b>a:
        return b 

# Écrire une fonction f8 qui prend trois nombres en entrée et qui retourne le plus grand des trois.
l=12
m=14
n=15

def f8(l,m,n):
    if (l>=m) and (l>=n):
        return l
    elif (m>=l) and (m>=n):
        return m
    else:
        return n
print(f8(10,10,5))
# (Au moins deux versions possibles : sans utiliser f7, et en utilisant f7).
def f8bis(l,m,n):
    max_lm=f7(l,m)
    max_n=f7(max_lm,n)
    return max_n
print(f8bis(111,122,15))

def f8bis_bis(l,m,n):
    return f7(f7(l,m),n)
# Écrire une fonction f9 qui prend un nombre et un mot en entrée, et qui affiche dans la console ce mot ce nombre de fois.
