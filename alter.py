import random

def n_len_rand(len_, floor=1):
    top = 10**len_
    if floor > top:
        raise ValueError(f"Floor {floor} must be less than requested top {top}")
    return f'{random.randrange(floor, top):0{len_}}'

print(n_len_rand(3))