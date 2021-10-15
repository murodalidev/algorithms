def count(n):
    if n != 0:
        print(n)
        count(n-1)
    return 0

print(count(10))


"""calculate faktorial with recusion"""
def faktorial(n):
    if n == 1:
        return 1
    else:
        return n * faktorial(n-1)
print(faktorial(5))