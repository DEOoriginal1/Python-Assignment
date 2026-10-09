def multiply_from_third_position(list):
	product = 1
	for content in list[2:len(list):3]:
		product = product * content
	return product
	
print(multiply_from_third_position([1,2,3,4,5,6,7,8,9,10]))	
	
