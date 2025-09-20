def bSearchInSortedList(lst: list[int], num: int) -> int:
    left: int = 0
    right: int = len(lst) - 1
    mid: int = (left + right) // 2
    while left <= right:
        print(left, right, mid)
        if lst[mid] == num:
            ar = lst[left:mid]
            res = bSearchInSortedList(ar, num)
            return mid if res == -1 else res + left
        elif lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return -1

numbers: list[int] = [1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15]
print(bSearchInSortedList(numbers, 15))