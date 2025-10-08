'''
num=int(input("Enter a number: "))

if num<0:
    print("Please enter positive numberr. ")
else:
    sum=0
    while num>0:
        sum=sum+num
        num -= 1
    print(sum)
'''
# Using Recursion

def Natural_Nos(n):
    
    if n<=1:
        return n
    else:
        return n + Natural_Nos(n-1)
    
n=int(input("Enter a number: "))

if n<=0:
    print("Enter a positive number")
else:
    print("Sum of the natural numbers till", n ,": ", Natural_Nos(n))

