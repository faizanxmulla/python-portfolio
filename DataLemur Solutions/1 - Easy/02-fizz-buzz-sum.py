def fizz_buzz_sum(target: int) -> int:
    return sum(i for i in range(target) if i % 3 == 0 or i % 5 == 0)

assert fizz_buzz_sum(10) == 23
