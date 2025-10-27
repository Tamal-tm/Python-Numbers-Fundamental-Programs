def findHCF(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x % i == 0 and y % i == 0:
            hcf=i
    return hcf
    
a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))

print("Hcf of given two numbers: ", findHCF(a,b))



