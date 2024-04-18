try:
    print(y)
except:
    print("exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")
