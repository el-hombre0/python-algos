from random import randint
from math import floor


def new_random_list(n, ness_num = False) -> list:
    new_list = list(0 for i in range(n))
    for i in range (n):
        new_list[i] = randint(-20,20)

    if(ness_num):
        random_position = randint(0, n - 1)
        new_list[random_position] = ness_num
    
    return new_list

