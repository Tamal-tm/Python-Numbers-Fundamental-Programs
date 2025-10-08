a=input("Enter a word: ")
rev=a[::-1] # Gap of -1

if a == rev:
    print(a, "is a palindrome.")
else:
    print("Not a palindrome.")