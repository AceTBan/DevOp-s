
# n : nombre de disques
# a : nom de la tour de départ
# b : nom de la tour intermédiaire
# c : nom de la tour de fin
def hanoi(n,a,b,c):
    if n == 0:
        return
    hanoi(n-1,a,c,b)
    print("Déplacer de",a,"vers",c)
    hanoi(n-1,b,a,c)    