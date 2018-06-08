def remainder(number, divisor):
    return number % divisor


assert remainder(6, 4) == 2
assert remainder(10, 3) == 1

assert remainder(20, divisor=7) == remainder(number=20, divisor=7)
assert remainder(divisor=7, number=20) == 20 % 7



