num=int(input("Enter a number: "))
order=len(str(num))
sum=0
temp=num

while temp>0:
    digit=temp%10
    cube=digit**order
    sum=sum + cube
    temp=temp//10

if sum == num:
    print('It is an armstrong number')
else:
    print("Not an armstrong number")
     
print("********************")

# Armstrong Number in an interval

lower=int(input("Enter lower limit here: "))
upper=int(input("Enter upper limit: "))


for num in range(lower, upper +1):
    sum=0
    temp=num
    order=len(str(num))
    while temp>0:
        digit=temp%10
        cube=digit**order
        sum=sum + cube
        temp=temp//10
    if sum == num:
        print(num)