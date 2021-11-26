# Écrire une fonction f1 qui ne prend rien en entrée, et qui affiche 17 dans la console.
def f1():
    print(17)
# Écrire une fonction f2 qui ne prend rien en entrée, et qui retourne 17.
def f2():
    return 17
# Utiliser la fonction f1 pour afficher 17 dans la console.
f1()
# Utiliser la fonction f2 pour afficher 17 dans la console.
print (f2())
# La fonction f2 a l'air moins pratique à utiliser. Quel intérêt pourrait-elle avoir par rapport à f1 ?

# Écrire une fonction f3 qui prend un nombre en entrée et qui affiche dans la console le double de ce nombre.
def f3(n):
    print(n*2)
     
# Écrire une fonction f4 qui prend un nombre en entrée et qui retourne le double de ce nombre.
def f4(n):
    return n*2
# Utiliser la fonction f3 pour écrire dans la console le double de 99.
f3(99)
# Utiliser la fonction f4 pour écrire dans la console le double de 99.
print(f4(99))
# Utiliser la fonction f4 pour stocker dans une variable appelée a le double de 99.
a=99
f4(a)
print(f4(a))
# Écrire une fonction f5 qui prend en entrée deux nombres et qui affiche dans la console la somme de ces deux nombres.
def f5(x,y):
    print(x+y)
# Écrire une fonction f6 qui prend en entrée deux nombres et qui retourne la somme de ces deux nombres.
def f6(l,m):
    return l+m
# Utiliser la fonction f5 pour écrire dans la console la somme de 42 et 77.
x=42
y=77
f5(x,y)

# Utiliser la fonction f6 pour écrire dans la console la somme de 42 et 77.
l=42
m=77
print(f6(l,m))
# Utiliser la fonction f6 pour incrémenter la variable a de la somme de 42 et 77.
a+=f6(l,m)