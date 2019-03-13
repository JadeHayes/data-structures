from binary import base_converter
from Expressions import postfixEval

# Convert the following values to binary using “divide by 2.” Show the stack of remainders.
print(base_converter(17, 2))
print(base_converter(45, 2))
print(base_converter(96, 2))


"""Convert the following infix expressions to prefix (use full parentheses)."""
# (A+B)*(C+D)*(E+F)
# + A B * + C D* + E F

# A+((B+C)*(D+E))
# + A + B C * + D E

# A * B * C * D + E + F
# ANS >>> + + * A  * B  * C D E F

"""Convert the above infix expressions to postfix (use full parentheses)."""
# (A+B)*(C+D)+ * E F + *

# A+((B+C)*(D+E))
#  A B C + D E + * +
#  stack iteration  # List iteration
#                   # A B C + D E + * +


""" Evaluate the following postfix expressions. Show the stack as each operand and operator is processed."""
# 2 3 * 4 +
# 1 2 + 3 + 4 + 5 +
# 1 2 3 4 5 * + * +

print(postfixEval("2 3 * 4 +"))
print(postfixEval('1 2 + 3 + 4 + 5 +'))
print(postfixEval('1 2 + 3 + 4 + 5 +'))
print(postfixEval('1 2 3 4 5 * + * +'))

"""
The alternative implementation of the Queue ADT is to use a list such 
that the rear of the queue is at the end of the list. What would this mean for Big-O performance?
"""
#  If a Queue were set up as a list, where the rear is the end. Big(O) performance for the methods:
# enqueue() -> O(n) # the rest of the list needs to shift as well
# dequeue() -> O(1)
# isEmpty() -> O(1)
# size() -> O(1) # in python it's O(1) we could loop through and count for O(n)

"""
What is the result of carrying out both steps of the linked list add method in reverse order? 
What kind of reference results? 
What types of problems may result?
"""
# Carrying out the `add` method in reverse order for a linked list you would set the head and then set the
# net node, which would break it because if the head was set before setting the current node's next,
# the head is what connects everything else, if the head wasn't connected you'd loose your list

"""Explain how the linked list remove method works when the item to be removed is in the last node."""
# When the last item is removed from the linked list, we set a variable `previous` to check the previous node.
# once our current Node is `None`, we know we are at the end of our linked list. We can then set our previous node's
# next to None, and our last node is removed from the list since it is nobody's next.


"""Explain how the remove method works when the item is in the only node in the linked list."""
# When the remove method is removing the only item in the list, it needs to check that the next node in the list
# is `None` and that the previous node in the list is also `None`.