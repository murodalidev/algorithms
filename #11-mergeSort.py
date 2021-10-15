def merge_sort(lst):
    if len(lst) > 1:

        mid = len(lst) // 2

        left = lst[:mid]
        print(left)

        right = lst[mid:]
        print(right)

        # Sorting the first half
        merge_sort(left)

        # Sorting the second half
        merge_sort(right)

        i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < right[j]:
            lst[k] = right[j]
            j += 1
            k += 1
        print(left)
        print(right)

def printList(arr):
	for i in range(len(arr)):
		print(arr[i], end=" ")
	print()

lst = [34, 25, 20, 5, 44, 12,9]
printList(lst)
print(merge_sort(lst))
printList(lst)



""" O(n) = n*log(n) """