# import new_random_list


def smallest_index(some_list, list_size) -> int:
    min_el = some_list[0]
    min_ind = 0
    for i in range(0, list_size):
        if (some_list[i] < min_el):
            min_el = some_list[i]
            min_ind = i
    return min_ind

# n = 10
# new_list = new_random_list.new_random_list(n)

# print(new_list, "\n", smallest_index(new_list, n))