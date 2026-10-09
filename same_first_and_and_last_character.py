def same_first_and_and_last_character(list):
	
	count = 0
	for content in list:
		count = count + 1
		if len(content) > 2 and content[0] == content[-1]:
			print (content + " " + ", The number of String is ", end = "") 
	print()
	print ("The number of String is in list is ", end = "")
	return count
			
print(same_first_and_and_last_character(['abc', 'xyz', 'aba', '1221', 'a', 'boba', 'racecar', 'aa']))

