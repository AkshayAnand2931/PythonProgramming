#Method 1
def fizz(num,res):
    if num % 3 == 0 :
        return 'Fizz'
    return ''

def buzz(num,res):
    if num % 5 == 0 :
        return 'Buzz'
    return ''

for num in range(0,101):
    res = ''
    res += fizz(num,res)
    res += buzz(num,res)
    if(res != ''):
        print(res)

#Method two
for num in range(0,101):
    if num % 3 == 0:
        if num % 5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif num % 5 == 0:
        print("Buzz")