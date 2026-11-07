# Function to check if a character is an alphabet
def check_alphabet(char):
    # Using the built-in isalpha() method
    if char.isalpha():
        print(f"'{char}' is an alphabet.")
    else:
        print(f"'{char}' is NOT an alphabet.")


# Example usage:
user_input = input("Enter a character: ")

# Checking if the user entered a single character
if len(user_input) == 1:
    check_alphabet(user_input)
else:
    print("Please enter exactly one character.")