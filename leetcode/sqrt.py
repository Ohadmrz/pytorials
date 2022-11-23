def sqrt_num(num: int) -> int:
    for i in range(1, num):
        if i * i == num:
            return i
        elif i * i > num:
            return i - 1
