# Using Anonymous Functions to display powers

nterms= int(input("Enter no. of terms: "))

# 'map' applies a function to every item in an iterable (range here).
# lambda x: 2 ** x → An anonymous function that takes x and returns 2 raised to power x.
# range(nterms+1) → Generates numbers from 0 up to 'nterms' inclusive.
# list(...) → Converts the map object into a list of results.

result=list(map(lambda x: 2 ** x, range (nterms+1))) # map will let the function (lambda x) perform on all the iterables. 

print(result)

for i in range(nterms+1):
    print("The value of 2 raised to the power", i, "is", result[i])



