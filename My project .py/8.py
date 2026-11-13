# Program to check if the entered age is between 10 and 20 years

# Take age input from the user
age = int(input("Enter your age: "))

# Outer conditional statement
if age >= 0:
  # Inner (nested) conditional statement
  if age >= 10:
    if age <= 20:
      print("The age is between 10 and 20 years.")
    else:
      print("The age is greater than 20 years.")
  else:
    print("The age is less than 10 years.")
else:
  print("Invalid age entered. Age cannot be negative.")