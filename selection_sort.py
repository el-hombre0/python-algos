# import new_random_list
import smallest_index
# from time import perf_counter

def selection_sort(some_list, list_size) -> list:
    new_list = list()
    for i in range (list_size):
        list_size = len(some_list)
        min_el = smallest_index.smallest_index(some_list, list_size)
        new_list.append(some_list.pop(min_el))
    return new_list

# N = 10
# not_sorted_list = new_random_list.new_random_list(N)
# print(not_sorted_list)

# start = perf_counter()
# print(selection_sort(not_sorted_list, N))
# end = perf_counter()
# print(f"Function execution have taken {end - start} s")
