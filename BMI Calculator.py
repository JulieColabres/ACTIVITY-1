# Get input for weight in kilograms
kg = float(input("Please input a weight in kg: "))

# Get input for height in meters
m = float(input("Please input a height in meters: "))

# Calculate BMI
x = kg / (m * m)

# Round BMI to 2 decimal places
x = round(x, 2)

# Output the result
print(f"Your BMI is {x}")
# NOTE: THIS CODE WAS WRITTEN IN C# AND CONVERTED TO PYTHON USING CHATGPT