def prime_factorial():
    num = int(input("Enter a number:  "))
    divisor = 2
    factors = []
    while num>= divisor:
        if num % divisor == 0:
            factors.append(divisor)
            num = num // divisor
        else:
            divisor += 1
    return factors

print(prime_factorial())
