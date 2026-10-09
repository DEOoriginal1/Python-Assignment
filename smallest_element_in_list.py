def smallest_element_in_list(list):

	smallest = list[0]
	
	for number in list:
		if number < smallest:
			smallest  = number
	return smallest
	
print(smallest_element_in_list([1,2,3,4,5,6,7,8,9,10]))
	
