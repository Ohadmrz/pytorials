def sum_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_digits(num // 10)


def harmonic_sum(num):
    if num == 1:
        return 1
    return 1/num + harmonic_sum(num-1)


def print_triangles(n):
    if n == 1:
        print('*')
        return
    elif n == 0:
        return

    # print(n * '*')
    print_triangles(n - 2)
    print(n * '*')



if __name__ == '__main__':
    print_triangles(5)