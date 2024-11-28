import sys
"""First we are going to validate the data"""
def validate_input(input_data):
    """Validate the input to ensure it contains only integers."""
    try:
        # Split the input by commas and convert to a list of integers
        return [int(x.strip()) for x in input_data.split(",")]
    except ValueError:
        print("Error: Invalid input. Please provide a list of integers separated by commas.")
        sys.exit(1)

def bitwise_operations(numbers):
    """Calculate AND, OR, and XOR of all integers in the list."""
    result_and = numbers[0]
    result_or = numbers[0]
    result_xor = numbers[0]

    for num in numbers[1:]:
        result_and &= num
        result_or |= num
        result_xor ^= num

    return result_and, result_or, result_xor

def filter_numbers(numbers, threshold):
    """Filter numbers greater than a given threshold."""
    return [num for num in numbers if num > threshold]

def main():
    # Check if input is provided
    if len(sys.argv) < 2:
        print("Error: No input provided.")
        sys.exit(1)

    # Get the input string from command-line arguments
    input_data = sys.argv[1]

    # Validate and parse input
    numbers = validate_input(input_data)

    # Perform bitwise operations
    and_result, or_result, xor_result = bitwise_operations(numbers)

    # Optional: Define a threshold value
    threshold = 4  # You can adjust this as needed

    # Filter numbers greater than the threshold
    filtered_numbers = filter_numbers(numbers, threshold)

    # Format the output
    print(f"Integers separated by commas: {', '.join(map(str, numbers))}")
    print(f"Threshold: {threshold}\n")
    print(f"Bitwise AND: {and_result}")
    print(f"Bitwise OR: {or_result}")
    print(f"Bitwise XOR: {xor_result}")
    print(f"Numbers greater than threshold: {filtered_numbers}")

if __name__ == "__main__":
    main()

