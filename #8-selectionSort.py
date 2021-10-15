def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i+1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
                # print(lst[min_index])
        lst[i], lst[min_index] = lst[min_index], lst[i]
        print(lst)
    return lst

lst = [64, 25, 12, 22, 11]
print('default -> ', lst)
print(selection_sort(lst))


"""O(n) = n**2"""