# Python intro

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