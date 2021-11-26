###########
# pikachu #
###########

# Première valeur : a
# Deuxième valeur : b
result = 0
for i in range(a):
    result += b

# Résultat : result

###########
# plafond #
###########

# Première valeur : a
# Deuxième valeur : b

result = 0
for i in range(a):
    result = b

# Résultat : result

###########
# tableur #
###########

# Première valeur : a
# Deuxième valeur : b

result = 0
for i in range(-1,a):
    result += b

# Résultat : result


#############
# wolverine #
#############

# Première valeur : a
# Deuxième valeur : b

result = 0
for i in range(a):
    for i in range(b):
        result += 1

# Résultat : result

# Nouvelle façon de décrire la même chose qu'au-dessus :
def wolverine(a,b):
    result = 0
    for i in range(a):
        for i in range(b):
            result += 1
    return result

###############
# ventilateur #
###############

# Première valeur : a
# Deuxième valeur : b

result = 0
for i in range(a,a):
    result += b

# Résultat : result

# Même chose avec la nouvelle écriture :
def ventilateur(a,b):
        result = 0
        for i in range(a,a):
            result += b
        return result

#######
# bob #
#######

# Première valeur : a
# Deuxième valeur : b
# Troisième valeur : c

result = 0
for i in range(a):
    for i in range(b):
        for i in range(c):
            result += 1

# Résultat : result

# Nouvelle écriture :
def bob(a,b,c):
    result = 0
    for i in range(a):
        for i in range(b):
            for i in range(c):
                result += 1
    return result

##########
# calcul #
##########

def calcul(a):
    result = 1
    for i in range(2,a+1):
        result *= i
    return result

##########
# python #
##########

def python(a):
    if a<2:
        return 1
    else:
        return a*python(a-1)

#############
# erogahtyp #
############

def erogahtyp(a):
    if a%2 == 0:
        return a//2
    else:
        return 3*a+1

#############
# pythagore #
#############

def pythagore(a,b):
    result = a
    for i in range(b):
        result = erogahtyp(result)
    return result

##############
# aceeilnrtt #
##############

def aceeilnrtt(a):
    result = 0
    while a != 1:
        a = erogahtyp(a)
        result += 1
    return result

###########
# micmath #
###########

def micmath(a,b):
    result = 0
    while a>=b:
        a /= b
        result += 1
    return result

#########
# stylo #
#########

def stylo(a,b):
    result = 1
    for i in range(b):
        result *= a
    return stylo

##########
# crayon #
##########

def crayon(a,b):
    result = 0
    for i in range(b):
        result *= a
    return result

#############
# minecraft #
#############

def minecraft(a):
    result = 1
    for i in range(a):
        result *= a
    return result

#########
# nenio #
#########

import random
import math
def nenio(a):
    result = random.random()
    result = math.floor(result)
    return result

#####################
# carapuceisamourai #
#####################

def carapuceisamourai(a):
    result = 1
    for i in range(a):
        result = 1-result
    return result

###################
# bouteilleidieau #
###################

def bouteilleidieau(a):
    if a<0:
        return 0
    elif a>0:
        return -1
    else:
        return 1

#############
# spiderman #
#############

def spiderman(a):
    result = 1
    for i in range(a):
        result = bouteilleidieau(result)
    return result

######
# gh #
######

def gh(a,b):
    return a&b

######
# jk #
######

def jk(a,b):
    return a|b

######
# lm #
######

def lm(a,b):
    return a^b

######
# wx #
######

def wx(a,b):
    return a<<b

######
# cv #
######

def cv(a,b):
    return a>>b
