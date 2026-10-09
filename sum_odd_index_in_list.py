def sum_odd_index_in_list(list):
	count = 0
	for number in range(len(list)):
		if number % 2 == 1 and number != 0:
			count = count + list[number]
	return count

	
print(sum_odd_index_in_list([19, 9, 47, 3, 13, 27, 13, 44, 28, 47]))

