def returning_duplicate_numbers(numbers):
	duplicate_numbers = []
	for index in range (len(numbers)):
		for count in range (index + 1, len(numbers)):
			if numbers[index] == numbers[count]:
				duplicate_numbers.append(numbers[index])
	return duplicate_numbers
	
	

list_array = [45,60,3,0,67,2,45,3,22,0]
result = returning_duplicate_numbers(list_array)

print(result)




