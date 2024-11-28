import sys

try:
    #User inputs from form.php
    input_numbers = sys.argv[1]
    threshold = int(sys.argv[2])
    
    numbers = list(map(int, input_numbers.split(',')))
    
    bitwise_and = numbers[0]
    bitwise_or = numbers[0]
    bitwise_xor = numbers[0]
    
    for num in numbers[1:]:
        bitwise_and &= num
        bitwise_or |= num
        bitwise_xor ^= num
    
    greater_than_threshold = [num for num in numbers if num > threshold]
    
    print(f"Bitwise AND: {bitwise_and}")
    print(f"Bitwise OR: {bitwise_or}")
    print(f"Bitwise XOR: {bitwise_xor}")
    print(f"Numbers greater than threshold: {greater_than_threshold}")

except (ValueError, IndexError):
    print("Invalid input. Please provide integers separated by commas and a valid threshold.")

