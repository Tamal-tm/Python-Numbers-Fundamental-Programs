num=int(input("Enter a number: "))
fact=1

if num<0:
    print("Factorial less than 0 does not exist.")

if num == 0:
    print("Factorial of 0 is", 1)

if num > 0:
    for i in range(1, num+1):
        fact=fact*i
    print("The factorial of a number is: ", fact)

# Using Recursion. 

def fact(a):
    if a==0:
        return 1
    else:
        return ((a) * fact(a-1))
    
num=int(input("Enter a number: "))
result=fact(num)
print('Factorial of the given number', result)