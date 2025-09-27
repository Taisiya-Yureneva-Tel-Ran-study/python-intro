def bSearchInSortedList(lst: list[int], num: int) -> int:
    left: int = 0
    right: int = len(lst) - 1
    mid: int = (left + right) // 2
    found: int = -1
    while left <= right and found == -1:
        if lst[mid] == num:
            res = bSearchInSortedList(lst[left:mid], num)
            found = mid if res <= -1 else (res + left)
        elif lst[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
    return found if found != -1 else -(left + 1)

def maxNegativeRepr(lst: list[int]) -> int:
    numSet: set[int] = set(lst)
    maxNeg: int = -1
    for num in lst:
        if num < 0 and -num in numSet:
            maxNeg = max(maxNeg, -num)
    return maxNeg
