def decorator(func):

    def inner(a,b,c):
        print("Something before the function")
        func(a,b,c)
        print("Something after the function")
    
    return inner

@decorator
def adder(a,b,c):
    print(a+b+c)

#adder = decorator(adder)
adder(1,2,3)