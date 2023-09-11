import sys as s
print("hello world")

x = 5
y = 5
print(type(x))
print(id(x))

#dynamically typed
x  = "hello"
print(type(x))
print(id(x))
print(s.getrefcount(5))

def add(x,y):
    return x+y

print(add(5,6))
print(100//3)
print(100/3)