import math


# def batches(n, my_list):
#     start_idx = 0
#     for i in range(math.ceil(len(my_list)/n)):
#         yield my_list[start_idx:start_idx+n]
#         start_idx =  start_idx + n
#

def batches(n: int, l: list):
    i = 0
    while i < len(l):
        yield l[i: i+n]
        i += n


if __name__ == '__main__':
    for batch in batches(10, list(range(105))):
        print(batch)