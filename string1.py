# Write a python program to accept a string and 
    print alternate characters starting 
    from first character

string=input()
n=len(string)
r=""
for i in range(0,n,2):
    r+=string[i]
print(r)
