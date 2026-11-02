points = [(2,3), (-1,4), (5,-6), (0,7), (-3,-2)]

def postive_points(point):
      index, counter = point
      return index > 0 and counter > 0
            
result_of_only_positives = filter(postive_points, points)
print(tuple(result_of_only_positives))

for index, counter in points:
      print(index,counter)
      

list_point = []      
for index, counter in points:
       list_point.append((index,counter))
print(list_point)




