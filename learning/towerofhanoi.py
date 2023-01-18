def tower(start,end,temp,num):
    '''The function to print the solution to tower of hanoi'''

    if num == 1:
        print("Move disk {} from {} to {}".format(num,start,end))
    else:
        tower(start,temp,end,num-1)
        print("Move disk {} from {} to {}".format(num,start,end))
        tower(temp,end,start,num-1)

num = int(input("Enter the number of disks to be arranged."))
tower('a','b','c',num)