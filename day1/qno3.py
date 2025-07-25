#QNO3:swapping no 
x=input("Enter value 1:")
y=input("Enter value 2:")
print("Before swapping x= ",x)
print("Before swapping y= ",y)
temp=0
temp=x
x=y
y=temp
print("After swapping x= ",x)
print("After swapping y= ",y)


"""ya code bi bilkul sahi h lakin pythonic way is ka ya h """
x=input("Enter value 1:")
y=input("Enter value 2:")
print("Before swapping x= ",x)
print("Before swapping y= ",y)
x,y=y,x
print("After swapping x= ",x)
print("After swapping y= ",y)