def func1(name):
    name = 'hi' + name

def func2(name):
    name = name[1:]

def func3(name):
    name = 'new name'

def func1list(num_list):
    num_list = [1,2] + num_list

def func2list(num_list):
    num_list = num_list[::-1]

def func3list(num_list):
    num_list = [10,20,30,40,50]

def func4list(num_list):
    num_list.extend([80,90])

name = 'ak'
print(name)
func1(name)
print(name)
func2(name)
print(name)
func3(name)
print(name)

num_list = [3,4,5,6,7]
print(num_list)
func1list(num_list)
print(num_list)
func2list(num_list)
print(num_list)
func3list(num_list)
print(num_list)
func4list(num_list)
print(num_list)