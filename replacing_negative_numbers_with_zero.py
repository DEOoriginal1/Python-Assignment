def replace_numbers_that_are_negative(numbers):
    for index in range (len(numbers)):
        if numbers[index] < 0:
            numbers[index] = 0
    return numbers
		
		
		
		
list_array = [5, -9, 3, 0, 2, 0]
result = replace_numbers_that_are_negative(list_array)

print(result)



