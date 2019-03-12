from binary import base_converter

# Convert the following values to binary using “divide by 2.” Show the stack of remainders.
print(base_converter(17, 2))
print(base_converter(45, 2))
print(base_converter(96, 2))

# Convert the following infix expressions to prefix (use full parentheses):
# (A+B)*(C+D)*(E+F)
# + A B * + C D* + E F

# A+((B+C)*(D+E))
# + A + B C * + D E

# A * B * C * D + E + F
# ANS >>> + + * A  * B  * C D E F
