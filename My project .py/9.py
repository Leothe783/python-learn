base = float(input("Enter the base number: "))
exponent = int(input("Enter the power (n): "))

result = 1

if exponent >= 0:
    for _ in range(exponent):
        result *= base
else:
    # Handle negative exponents by multiplying base (-(exponent)) times and taking reciprocal
    for _ in range(-exponent):
        result *= base
    result = 1 / result

print(f"{base} raised to the power of {exponent} is {result}")