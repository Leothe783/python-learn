num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary: 0")
else:
    temp = num
    binary = ""
    while temp > 0:
        remainder = temp % 2
        for _ in range(1):
            binary = str(remainder) + binary
        temp = temp // 2

    print("Binary:", binary)