# write an algorithm that will read a string of parentheses
# from left to right and decide whether the symbols are balanced.

from Stacks import Stack


def is_balanced(parens: str):
    """Checks to see if a string of parens are balanced"""
    stack = Stack()

    try:
        for paren in parens:
            if stack.is_empty() or (not stack.is_empty() and paren == stack.peek()):
                stack.push(paren)
            else:
                stack.pop()
        return stack.is_empty()
    except IndexError:
        return False


print(is_balanced("((((()"))
print(is_balanced("()"))
print(is_balanced("(((()(()"))
print(is_balanced("(((())))"))
print(is_balanced("()()"))
print(is_balanced(""))
