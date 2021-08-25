left: int = int(input("Left hand side: "))
right: int = int(input("Right-hand side: "))

product: str = str(left ** right)
float_div: str = str(left / right)
floor_div: str = str(left // right)
remainder: str = str(left % right)

print(str(left) + " ** " + str(right) + " is " + product)
print(str(left) + " / " + str(right) + " is " + float_div)
print(str(left) + " // " + str(right) + " is " + floor_div)
print(str(left) + " % " + str(right) + " is " + remainder)
