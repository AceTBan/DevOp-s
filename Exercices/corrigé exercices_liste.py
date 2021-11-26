# 1) Créer un tableau l1 de 6 cases, qui contient les nombres 144, 202, 216, 216, 222 et 64.
l1 = [144,202,216,216,222,64]
print(l1)

# 2) Ajouter le nombre 0 à la fin du tableau l1.
l1.append(0)
print(l1)

# 3) Afficher *un par un* tous les éléments du tableau l1.
print(l1[0])
print(l1[1])
print(l1[2])
print(l1[3])
print(l1[4])
print(l1[5])
print(l1[6])

# 4) Retirer le dernier élément du tableau l1.
l1.pop()

# 5) Créer un tableau l2 qui contient les nombres 238, 222, 228, 216, 200.
l2 = [238,222,228,216,200]

# 6) Ajouter le nombre 58 à la fin de l2.
l2.append(58)

# 7) Ajouter *un par un* tous les éléments du tableau l2 à la fin du tableau l1.
#l1.append(l2[0])
#l1.append(l2[1])
#l1.append(l2[2])
#l1.append(l2[3])
for i in range(len(l2)):
    l1.append(l2[i])

# 8) Afficher *un par un* tous les éléments du tableau l1.
for i in range(len(l1)):
    print(l1[i])

# 9) Retirer et stocker dans la variable ma_variable le dernier élément du tableau l1.
ma_variable = l1.pop()
print(ma_variable)
print(l1)

# 10) Afficher la taille du tableau l1.
print(len(l1))

# 11) Ajouter le nombre 66 à la fin du tableau l1.
l1.append(66)

# 12) Diviser par 2 toutes les variables contenues dans le tableau l1.
#l1[0] = l1[0]/2
#l1[1] = l1[1]/2
#...
for i in range(len(l1)):
    l1[i] = l1[i]/2

# 13) Tester le code suivant pour vérifier si vous avez le bon résultat à la fin (le but n'est pas de chercher à comprendre ce code) :
from functools import reduce
print(reduce(lambda x,y:x+chr(int(y)),l1,""))
print(chr(ma_variable)+chr(ma_variable-17))