#Write a python program to accept a string and
    print only consonants in the given left to right order

string=input()
vowels=['a','e','i','o','u']
n=len(string)
r=""
for i in range(n):
     if string[i] not in vowels:
        r+=string[i]
print(r)
