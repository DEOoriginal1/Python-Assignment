def swap(numbers):
      new_array = []
      for index in range (len(numbers)):
            result = numbers[len(numbers) - index - 1]
            new_array.append(result)
      
      return new_array
     
def multiple_arrays(numbers):
      for index in range (len(numbers)):
            numbers[index] = swap(numbers[index]);
      
      return numbers;



matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]];

print(multiple_arrays(matrix));





#def swap(numbers):
#      new_list = []
#      
#      for index in numbers:
#            new_list.append(index[::-1])
#      return new_list
#      
#matrix = [[1,2,3], [4,5,6], [7,8,9]]
#print(swap(matrix))
