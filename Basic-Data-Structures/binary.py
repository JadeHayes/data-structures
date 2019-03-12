from pythonds.basic.stack import Stack


def base_converter(decimal: int, base:int) -> str:
    digits = "0123456789ABCDEF"
    stack = Stack()

    while decimal > 0:
        remainder = decimal % base
        stack.push(remainder)
        decimal = decimal // base

    ans = ""
    while not stack.isEmpty():
        ans += digits[stack.pop()]

    return ans


base_converter(25, 2)
base_converter(888, 18)
base_converter(28, 11)
base_converter(100, 12)
base_converter(3, 8)
