try:
    a=10/0
except:
    print("division by zero exception occured")
else:
    print(a,"No exception occured")
finally:
    print("Finally is executed")
print("outside the try block")
