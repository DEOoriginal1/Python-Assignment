def is_a_prime(number):
	for count in range(2, int(number**0.5) + 1):
		if(number % count == 0):
			return False
		if(count == 2):
			return True
	
def sort_prime_numbers(numbers):
	prime_numbers = []
	for number in numbers:
		if is_a_prime(number):
			prime_numbers.append(number)
			
	prime_numbers.sort()
	return prime_numbers
	
	
	
list_array = [5,9,3,6,2]
result = sort_prime_numbers(list_array)


print(result)
	
