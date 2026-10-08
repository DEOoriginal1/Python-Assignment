def length_of_string(word):
	return len(word)
	
	
def first_last_two_letter(word):
	if len(word) > 1:
		print (word[0],word[1],word[len(word)-2],word[len(word)-1], sep = "",end = "")
	return ""	


def add_extra_word(word):
	if word[-3:] == "ing":
		return word+"ly"
	if len(word) >= 3:
		return word+"ing"
	if len(word) < 3:
		return word	


def longest_word_and_length_in_list(word):

	highest_word = word[0]
	highest_length = len(word[0])
	for content in word:
		if len(content) > highest_length:
			highest_length = len(content)
			highest_word = content


	print(highest_word, ",",highest_length, sep = "",end = "")
	return ""
		
	
			
def odd_index_remover(word):
	return word[1::2]

	
def minimum_in_list(numbers):

	smallest_number = numbers[0]
	for number in numbers:
		if number < smallest_number:
			smallest_number = number
	return smallest_number



def maximum_in_list(numbers):

	highest_number = numbers[0]
	for number in numbers:
		if number > highest_number:
			highest_number = number
	return highest_number	


def string_number_repetion(word,number):
	if number.is_integer():
		return word * number
	else:
		return word

	
def list_square(numbers):
	square_list = []
	for number in numbers:
		number = number ** 2
		square_list.append(number)
	return square_list

	
def sum_of_list_square(numbers):
	square_list = []
	sum_of_number = 0
	for number in numbers:
		number = number ** 2
		square_list.append(number)
	for number in square_list:
		sum_of_number = sum_of_number + number
	return sum_of_number	


print(length_of_string("SEMICOLON"))
print(first_last_two_letter("semicolon"))
print(first_last_two_letter("on"))
print(first_last_two_letter("o"))
print(add_extra_word("abc"))
print(add_extra_word("string"))
print(add_extra_word("on"))
print(longest_word_and_length_in_list(['welcome','out','weather','mobile','breakfast','journey']))
print(odd_index_remover("semicolon"))
print(minimum_in_list([8,4,9,2,5,7,3]))
print(maximum_in_list([8,4,9,2,5,7,3]))
print(string_number_repetion("hello",3))
print(string_number_repetion("hi",4.5))
print(list_square([2,3,4,5,7]))
print(sum_of_list_square([2,3,4,5,7]))
