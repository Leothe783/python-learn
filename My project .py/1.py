# Program to check if the temperature is suitable for wearing light clothes

# Take temperature input from the user
temperature = float(input("Enter the current temperature in °C: "))

# Conditional statements to decide clothing
if temperature >= 28:
    print( 'warm summer day! You can wear light and soft clothes.')
elif 22 <= temperature < 28:
    print("The weather is pleasant. Light clothes are fine, but keep a light jacket handy.")
else:
    print("It's too cold for light clothes! Better wear a jacket or pullover to avoid catching a cold.")