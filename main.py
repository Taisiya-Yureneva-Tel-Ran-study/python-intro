def bSearchInSortedList(lst: list[int], num: int) -> int:
    left: int = 0
    right: int = len(lst) - 1
    mid: int = (left + right) // 2
    while left<right:
        mid = (left + right) // 2
        if lst[mid] >= num:
            right = mid
        else:
            left = mid + 1
    return left if lst[left] == num else -(left + 1)

def isSumTwo(lst: list[int], sum: int) -> bool:
    setNums: set[int] = set()
    for num in lst:
        if sum - num in setNums:
            return True
        setNums.add(num)
    return False

def maxNegativeRepr(lst: list[int]) -> int:
    numSet: set[int] = set(lst)
    maxNeg: int = -1
    for num in lst:
        if num < 0 and -num in numSet:
            maxNeg = max(maxNeg, -num)
    return maxNeg
