
a=0
b=1
num=int(input("Enter no. of terms: "))
if num == 1:
    print(a)
    
else:
    print(a)
    print(b)
    for i in range(1, num-1):
        c=a+b
        a=b
        b=c
        print(c)
        
# Using Recursion

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

num=int(input("Enter no. of terms: "))
if num <= 0:
    print("Enter a positive no.")
else:
    print("Fibonacci series: ")
    for i in range(num):
        print(fibo(i))
















