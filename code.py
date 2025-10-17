# Hands-On: Write basic Python programs (e.g., temperature converter)

# This program converts temperature between Celsius and Fahrenheit.

def temperature_converter():
    print("=== Temperature Converter ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.2f}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F = {celsius:.2f}°C")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Run the program
temperature_converter()

# Client Project: Create a basic data processing script
# Example: Calculating the average temperature from a list of temperature readings

def calculate_average_temperature(temperatures):
    """
    This function takes a list of temperature values
    and returns their average.
    """
    total = sum(temperatures)
    count = len(temperatures)
    average = total / count
    return average

def main():
    print("=== Client Project: Average Temperature Calculator ===")
    
    # Ask user how many temperature readings to process
    temperatures = []
    n = int(input("Enter the number of temperature readings: "))
    
    for i in range(n):
        temp = float(input(f"Enter temperature {i+1}: "))
        temperatures.append(temp)

    # Calculate average
    avg_temp = calculate_average_temperature(temperatures)

    print("\n--- Temperature Report ---")
    print(f"Temperatures entered: {temperatures}")
    print(f"Average Temperature: {avg_temp:.2f}°C")

# ✅ This ensures the main() function runs only when the script is executed directly
if __name__ == "__main__":
    main()

