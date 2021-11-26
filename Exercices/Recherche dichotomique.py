def dicho(n,l,i1,i2):
    if i1 > i2:
        return False
    milieu = (i1+i2)//2
    print('Je regarde la case numéro',milieu)
    if l[milieu] == n:
        return True
    elif l[milieu] > n:
        return dicho(n,l,i1,milieu-1)
    else:
        return dicho(n,l,milieu+1,i2)
    
def search(n,l):
    return dicho(n,l,0,len(l)-1)