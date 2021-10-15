def addNums(a, b, c):
    summa = a + b + c
    return summa

def getLargest(a,b,c):
    if a>b:
        if a>c:
            return a
        else: 
            return c
    else:
        if b>c:
            return b
        else:
            return c

            
a,b,c=20,8,10
print(getLargest(a, b, c))