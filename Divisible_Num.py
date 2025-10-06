# Finds numbers divisible by another number ex. 13

for i in range(1,100):
    if i%13==0:
        print(i)

# Using lambda function and filter()

l=[35,12,87,34,90,11,26,7,46,53, 87, 39]

# The filter() function in Python is a built-in function used to construct an iterator 
# from elements of an iterable for which a function returns true. It offers an efficient
# way to select specific items based on a given condition.

result=list(filter(lambda x : x % 13 == 0, l))

print("The numbers divisible by 13 are: ",result)