def largest_element_in_list(list):

	largest = list[0]
	
	for number in list:
		if number > largest:
			largest = number
	return largest
	
print(largest_element_in_list([1,2,3,4,5,6,7,8,9,10]))
	
