def digit_sum(n):
    total = 0
    for i in range (1, 1+n):
        if i % 2 == 0:
        	continue
        if i % 2 == 1:
        	return total += i
        elif i % 10 == 0:
    		return 1
       
       
       
print(digit_sum(123))
