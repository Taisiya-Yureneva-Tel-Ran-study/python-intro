# Python intro

## HW 22 Tasks for figuring out O[N] solutions

### Function isSumTwo
Takes two parameters: list of integer numbers (numbers) and one integer number (sum)

Returns True (T should be capital) if the given list (numbers) contains two items, sum of which equals the given number (sum), otherwise returns False

Examples
isSumTwo([1, 2, 3, 4], 4) -> True
isSumTwo([1, 2, 3, 4], 2) -> False
##### Unit tests
Unit tests in a separate file (module)

### Function maxNegativeRepr
Takes one parameter: list of integer numbers (numbers)

Returns either maximal positive number from the given list having its negative representation or -1 if no any

Examples
* maxNegativeRepr(100, 4, 1, -1, -4, -100) -> 100
* maxNegativeRepr(100, 4, 1, 1, 4, 100, -1) -> 1
* maxNegativeRepr(100, 4, 1, 1, 4, 100, 1, -2) -> -1
##### Unit tests
Unit tests in a separate file (module)

## HW #21

### Function bSearchInSortedList
1. In case there are several occurrences of the number being searched, the function
returns the index of the first occurrence

    a. Keep O[LogN] complexity

    b. Example: numbers = [20, 20, 20, 20, 20],

        - bSearchInSortedList(numbers, 20)
    
        - returns 0

2. In case there is no occurrence of the number being searched in the list, the function 
returns a negative number such that its absolute value minus 1 gives the index,
by which the searched number might be inserted in the list keeping sorted order

    * Example: numbers = [20, 30, 40, 50, 60], bSearchInSortedList(numbers, 45) returns -4