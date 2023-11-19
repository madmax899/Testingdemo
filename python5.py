# Sample list
numbers = [3, 7, 1, 9, 2]

# Initialize max_number with the first element of the list
max_number = numbers[0]

# Use a for loop to iterate through the list
for num in numbers:
    max_number = max(max_number, num)

# Print the result
print("The max number in the list is", max_number)
 
