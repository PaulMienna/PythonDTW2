x = 5
y = 10
z = x + y
print(z)

if z > 7:
    print("z is greater than 7")

def additive(a: int, b: int):
    result =a+b
    message= f"{a} plus {b} equals {result}"
    return message

print(additive(5, 2))

def multiply(a: int, b: int):
    result =a*b
    message= f"{a} times {b} equals {result}"
    return message

print(multiply(7, 9))
