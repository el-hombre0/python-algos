import new_random_list
import selection_sort
from math import floor

def binnary_search(some_list, elem):
    low = 0
    high = len(some_list) - 1

    while (low <= high):
        mid = floor((low + high) / 2)
        if(elem != some_list[mid]):
            if (elem > some_list[mid]):
                low = mid
            else:
                high = mid
        else:
            return mid
    return mid

elem = 5
N = 10
arr = selection_sort.selection_sort(new_random_list.new_random_list(N, elem), N)
print (arr, "elem: ", elem)
print(binnary_search(arr, elem))