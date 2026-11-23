ecimal = int(input("Enter a decimal number: "))
binary = ""

# Outer loop runs once for the number, inner loop extracts binary digits
for _ in range(1):
    temp =
    if temp == 0:
        binary = "0"
    while temp > 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2

print("Binary number:", binary)