import bisect

numbers: list[int] = []
bisect.insort(numbers, 10)
bisect.insort(numbers, 50)
bisect.insort(numbers, 30)
bisect.insort(numbers, 13)
bisect.insort(numbers, 3)

print(numbers)

def getNumbersRange(arr: list[int], min: int, max: int) -> list[int]:
    res: list[int] = []
    for num in arr:
        if min <= num <= max:
            res.append(num)
    return res

print(getNumbersRange(numbers, 10, 30))

def getSortedNumbersRange(arr: list[int], min: int, max: int) -> list[int]:
    left: int = bisect.bisect_left(arr, min)
    right: int = bisect.bisect_right(arr, max)
    res: list[int] = arr[left:right]
    return res

print(getSortedNumbersRange(numbers, 10, 30))
