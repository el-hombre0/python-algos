from random import randint
# from new_random_list import new_random_list


def my_quick_sort(some_list) -> list:
    list_size = len(some_list)

    if (list_size < 2):
        return some_list

    else:

        pivot = some_list[randint(0, list_size - 1)]

        less = [i for i in some_list[1:] if i <= pivot]

        greater = [i for i in some_list[1:] if i > pivot]
        return my_quick_sort(less) + [pivot] + my_quick_sort(greater)


# N = 10

# current_list = new_random_list(N)
# print(current_list)
# print(my_quick_sort(current_list))
