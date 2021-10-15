
def faktorial(n):
    i=1
    pivot=1
    while i!=n+1:
        pivot = pivot*i        
        i += 1
    return pivot

print(faktorial(5))


"""another way"""
n = int(input('enter n: '))
pivot = 1
for i in range(1, n+1):
    pivot *= i
print(pivot)