def short_function():
    return 1


def a_really_long_function_that_should_get_flagged():
    total = 0
    total += 1
    total += 2
    total += 3
    total += 4
    total += 5
    total += 6
    total += 7
    total += 8
    total += 9
    total += 10
    total += 11
    total += 12
    total += 13
    total += 14
    total += 15
    total += 16
    total += 17
    total += 18
    total += 19
    total += 20
    total += 21
    total += 22
    total += 23
    total += 24
    total += 25
    total += 26
    total += 27
    total += 28
    total += 29
    total += 30
    return total


def calculate_price():
    tax_rate = 47
    return tax_rate