while True:
    numerator, denominator = input().split()
    if numerator == '0' and denominator == '0':
        break
    numerator = int(numerator)
    denominator = int(denominator)

    mixed = numerator//denominator
    numerator = numerator%denominator
    print(mixed, numerator, '/', denominator)