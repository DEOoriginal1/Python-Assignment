def move_all_zeros(numbers):
	numbers = []
	zero_numbers = []
	for index in range (len(numbers)):
		if numbers[index] == 0:
			zero_numbers[index].append(0)
		else:
			numbers[index].append(index)
	return numbers + zero_numbers
		
		

list_array = [5,0,3,0,2,0]
result = move_all_zeros(list_array)

print(result)





