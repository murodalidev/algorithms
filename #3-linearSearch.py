n = int(input("array length n: "))
t = int(input("wanten number t: "))
def linear_search(n, t):
    for i in range(0, n-1):
        if i == t:
            return(f'wanted number is {t} | index is equal to {i}')

print(linear_search(n, t))

"""O(n) = n"""