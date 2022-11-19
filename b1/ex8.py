def perfect(number:int ) -> bool :
    dividers = []
    if number == 0:
        return False
    for i in range (1,number):
        if number % i == 0:
            dividers.append(i)
    if sum(dividers) == number:
        return True
    else:
        return False
print(perfect(496))