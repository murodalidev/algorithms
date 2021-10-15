lst = [i*2 for i in range(10)]
print(lst)
class Search:
    def binary(lst, item):
        first = 0
        last = len(lst) - 1
        found = False
        while first <= last and not found:
            mid = (first + last) // 2
            if lst[mid] == item:
                found = mid
            else:
                if lst[mid] < item:
                    first = mid + 1
                else:
                    last = mid - 1
        return found

print(Search.binary(lst, 4))


"""O(n) = log(n)"""