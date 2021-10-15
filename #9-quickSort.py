# from random import randrange
# def qsort(lst):
#     if len(lst) < 2:
#         return lst
#     else:
#         # pivot = lst.pop(0)
#         pivot = lst.pop(randrange(len(lst) - 1))
#         less = [i for i in lst if i < pivot]
#         big = [i for i in lst if i > pivot]
#         print(f'{less} + [{pivot}] + {big}')
#         return qsort(less) + [pivot] + qsort(big)

# lst = [1, 5, 12, 0, -5, 66]
# # lst = list(range(20))
# print('default: ', lst)
# print('result: ', qsort(lst))


"""O(n) = n*log(n)"""