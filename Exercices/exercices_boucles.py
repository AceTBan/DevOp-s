# Exercice 1 : écrire 50 fois "Bonjour" dans la console.

# for _ in range(50):
#     print('bonjour')

# Exercice 2 : écrire dans la console :
# A
# B
# A
# B
# A
# B
# A
# B
# A
# B

# for _ in range(5):
#     print('A')
#     print('B')

# Exercice 3 : écrire dans la console :
# A
# A
# A
# A
# A
# B
# A
# A
# A
# A
# A
# B
# A
# A
# A
# A
# A
# B

# for _ in range(3):
#     for _ in range(5):
#         print('A')
#     print('B')

# Exercice 4 : écrire dans la console :
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# for n in range(10):
#     print(n) 

# Exercice 5 : écrire dans la console :
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12

# n=2
# for _ in range(10):
#     n+=1
#     print(n)

# Exerice 6 : écrire dans la console :
# 0
# 1
# 2
# 3
# 0
# 1
# 2
# 3
# 0
# 1


# n=-1
# for _ in range(2):
#     for _ in range(4):
#         n += 1
#         if n==4 :
#             n=0
#         print(n)
# print(0)
# print(1)


# Exercice 7 : écrire dans la console :
# 0
# 1
# 2
# 3
# 4
# A
# A
# A
# 8
# 9

# for n in range(10):
#     if n>4 and n<8:
#         n='A'
#     print(n)


# Exercice 8 : écrire dans la console :
# 100
# 1
# 2
# 103
# 4
# 5
# 106
# 7
# 8
# 109

# for n in range(10):
#     if n%3 == 0:
#         n += 100
#     print(n)

# Exercice 9 : écrire dans la console :
# 0
# 101
# 202
# 3
# 104
# 205
# 6
# 107
# 208
# 9

# for n in range(10):
#     if n%3 ==0:
#         n+=0
#     elif n%3 ==1:
#         n+=100
#     else:
#         n+=200
#     print(n)

# Exercice 10 : écrire dans la console tous les résultats possibles de lancers de deux dé :
# 1 1
# 1 2
# 1 3
# ...
# 6 4
# 6 5
# 6 6

# for i in range(6):
#     for n in range(6):
#         print(i+1 , n+1)

# Exercice 11 : adapter l'exercice précédent pour enlever les doublons (on ne veut pas afficher 1 2 et 2 1, mais seulement l'un des deux).

for i in range(6):
    for n in range(6):
        print( i+1 , n+1 )
    


# Exercice 12 : en prenant des dés à 20 faces, combien de résultats différents (sans doublon) peut-on afficher ? (Autrement dit : adapter le code précédent pour compter les résultats au lieu de les afficher)

# Exercice 13 : afficher la table de multiplication de 1 (de 1 à 9):
# 1x1 = 1
# 1x2 = 2
# 1x3 = 3
# 1x4 = 4
# 1x5 = 5
# 1x6 = 6
# 1x7 = 7
# 1x8 = 8
# 1x9 = 9

# Exercice 14 : que faut-il modifier du code précédent pour obtenir la table de 2 :
# 2x1 = 2
# 2x2 = 4
# 2x3 = 6
# 2x4 = 8
# 2x5 = 10
# 2x6 = 12
# 2x7 = 14
# 2x8 = 16
# 2x9 = 18

# Exercice 15 : comment généraliser pour afficher toutes les tables de multiplication de 1 à 9 :
# 1x1 = 1
# 1x2 = 2
# 1x3 = 3
# 1x4 = 4
# ...
# 9x7 = 63
# 9x8 = 72
# 9x9 = 81

# Exercice 16 : calculer 1+2+3+4+...+99+100. (Vous devriez trouver 5050)

# Exercice 17 : trouver le nombre n tel que 1+2+3+4+5+...+(n-1)+n = 302253

# Exercice 18 : Afficher :
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
