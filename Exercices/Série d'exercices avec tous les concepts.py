# Fonction qui prend un tableau en entrée et affiche le dernier élément de ce tableau.

def affiche_le_dernier():
    list1=[1,3,5,7,9]
    print(list1[-1])
affiche_le_dernier()    

# Fonction qui prend un tableau en entrée et retourne le dernier élément de ce tableau.

def retourne_le_dernier():
    list2=[92,6,4,8]
    return list2[-1]

# Fonction qui prend en entrée un tableau et qui retourne le minimum de ce tableau.

def retourne_le_mini(l):
    return min(l)
print(retourne_le_mini([1,2,3,5,8]))

# Fonction qui prend en entrée un tableau et qui retourne le maximum de ce tableau.

def retourne_le_max(l):
    return max(l)
print(retourne_le_max(l=[5,6,3,2]))

# ++ Fonction qui prend en entrée un tableau de nombres positifs et qui retourne la deuxième plus grande valeur du tableau.

def la_deuxième_plus_grande():
    list5=[7,5,9,2]
    list.sort()
    return list5[-2]
    
# # correction:
# def deuxieme_plus_grand(l):
#    pg = 0
#    pg2 = 0
#    for i in range(len(l)):
#        if l[i] > pg:
#            pg2 = pg
#            pg = l[i]
#         elif l[i] > pg2:
#             pg2 = l[i]
#     return pg2

# Fonction qui prend en entrée un tableau et un nombre et qui retourne le nombre de fois que ce nombre apparaît dans le tableau.

# Fonction qui prend en entrée un tableau et un nombre et qui retourne True si le nombre existe dans le tableau, False sinon.

# Variante de l'exo : on **sait** que le tableau reçu est trié (on ne le vérifie pas)