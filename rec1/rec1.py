def sum_digits(num):
    if num == 0:
        return 0

    return num % 10 + sum_digits(num // 10)


def harmonic_sum(num):
    if num == 1:
        return 1
    return 1/num + harmonic_sum(num-1)


def chocolates(money, wraps, price, wraps_needed):
    if money < price and wraps < wraps_needed:
        return 0

    if wraps == wraps_needed:
        return 1

    return 1 + chocolates(money-price, wraps+1, price, wraps_needed)


if __name__ == '__main__':
    print(chocolates(16, 0, 2, 2))