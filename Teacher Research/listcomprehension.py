num_list = [num for num in range(0,100) if num % 3 == 0]
print(num_list)

num_list = [min(x,y) for x in [2,5,100,56] for y in [1,5893,9,23]]
print(num_list)

num_list = [x if x<y else y for x in [2,5,100,56] for y in [1,5893,9,23]]
print(num_list)