from pythonds.basic.stack import Stack
# develop an algorithm to convert any infix expression to a postfix expression

def infix_to_postfix(infix: str):
    """Takes an infix expression and converts it to postfix."""
    prec = {} # dictionary to hold precedence of different values
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    post_fix: list = []
    token: list =infix.split()

    for t in token:
        if t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or t in "0123456789":
            post_fix.append(t)
        elif t =="(":
            opStack.push(t)
        elif t ==")":
            top_token = opStack.pop()
            while top_token != "(":
                post_fix.append(top_token)
                top_token = opStack.pop()
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[t]):
                post_fix.append(opStack.pop())
            opStack.push(t)
    while not opStack.isEmpty():
        post_fix.append(opStack.pop())
    return  " ".join(post_fix)


print(infix_to_postfix("A * B * C * D + E + F"))
