# Write a python program to accept a string and 
    print whether it is a palindrome or not 

string=input()
reverse=string[::-1]
if string == reverse:
    print("It is Palindrome")
else:
    print("It is not a Palindrome")
