def average_of_list_elememts(list):
	sum_of_elements = 0
	for content in list:
		sum_of_elements = sum_of_elements + content
	average = sum_of_elements / len(list)
	return average
	
print(average_of_list_elememts([1,2,3,4,5,6,7,8,9,10]))
