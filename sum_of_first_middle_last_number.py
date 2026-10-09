def sum_of_first_middle_last_number(list):
	first_index = list[0]
	last_index = list[-1]
	middle = len(list) // 2
	
	if len(list) % 2 == 0:
		middle_index = (list[middle - 1] + list[middle])/2
	else:
		middle_index = list[middle]
		
	return first_index + middle_index + last_index
	
print(sum_of_first_middle_last_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
print(sum_of_first_middle_last_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))	
	
