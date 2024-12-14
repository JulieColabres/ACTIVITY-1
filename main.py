def main():
    print("Please input a temperature scaling to convert into.")
    print(">celsius")
    print(">fahrenheit")
    
    # Read the user input and convert it to lowercase for case insensitivity
    x = input().lower()
    z = 0
    v = 0.0
    
    # Switch-like structure in Python using if-elif
    if x == "celsius":
        print("Fahrenheit to Celsius chosen.")
        v = 1.8
        z = 32
    elif x == "fahrenheit":
        print("Celsius to Fahrenheit chosen.")
        v = 0.6
        z = -32
    else:
        print("That is not a valid temperature scale.")
        return  # Exit the function early
    
    # Ask for the temperature value
    print("Please input a number.")
    y = int(input())  # Convert the input to an integer
    
    # Calculate the converted temperature
    c = (v * y) + z
    print(f"Temperature {y} in {x} is equal to = {c}")

# Run the main function
if __name__ == "__main__":
    main()
# NOTE: THIS CODE WAS WRITTEN IN C# AND CONVERTED TO PYTHON USING CHATGPT