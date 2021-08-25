"""Relational ops"""

__author__ = "730155204"


left: int = int(input("Left hand side: "))
right: int = int(input("Right-hand side: "))

less: str = str(left < right)
greater_or_equal: str = str(left >= right)
equal: str = str(left == right)
not_equal: str = str(left != right)

print(str(left) + " < " + str(right) + " is " + less)
print(str(left) + " >= " + str(right) + " is " + greater_or_equal)
print(str(left) + " == " + str(right) + " is " + equal)
print(str(left) + " != " + str(right) + " is " + not_equal)