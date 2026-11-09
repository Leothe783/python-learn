# Congratulations message
# This program demonstrates various Python string operations to create a personalized congratulatory message.

# 1. Define variables for the student's name and achievement
student_name = " alex smith "
achievement = "Python Programming Champion"

# 2. String Methods & Operations
# .strip() removes extra whitespace from the name
cleaned_name = student_name.strip()

# .title() capitalizes the first letter of each word properly
formatted_name = cleaned_name.title()

# String Concatenation (+) to combine strings
full_message = "Congratulations, " + formatted_name + "!"

# String Multiplication (*) to create decorative banner lines
banner = "=" * 45

# 3. Print the final styled message
print(banner)
print(full_message)
print("You have successfully won the award for:")
print(achievement.upper())  # .upper() converts the string to all uppercase letters
print(banner)

# 4. Display additional string length information
print("\nFun Fact:")
print("Your name has", len(formatted_name), "characters in it.")