def buble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            print('\t', lst)
        print(lst)
    return lst

lst = [64, 34, 25, 12, 82, 90, 11]
print(lst)
print(buble_sort(lst))

""" O(n) = n**2 """