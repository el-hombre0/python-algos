import random
def new_random_list(n) -> list:
    arr = list(0 for i in range(n))
    for i in range (n):
        arr[i] = random.randint(1,50)
    return arr
