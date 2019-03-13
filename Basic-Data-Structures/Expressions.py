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
        #  If the token we are on isn't an operator or (, add it to the postfix list
        # list because the position of the letters and numbers do not change.
        if t in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or t in "0123456789":
            post_fix.append(t)
        # If the token is a opening paren "(" it means there will be a closing
        # paren we need to translate this to postfix, pop it on the stack.
        elif t =="(":
            opStack.push(t)
        # if the token is a closing paren
        elif t ==")":
            top_token = opStack.pop()
            while top_token != "(":
                post_fix.append(top_token)
                top_token = opStack.pop()
        # If the token is an operator, check to see if the opstack is empty and if the
        # tokens precedence is > or = the top token on the stack.
        # if it's greater than, it will be calculated first, so put it in the list.
        else:
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[t]):
                post_fix.append(opStack.pop())
            # if the stack is empty or the precedence is less than, put the token on the top of the stack.
            #  this way the lower precedence operators will get added to the list first.
            opStack.push(t)
    # after we've gone through all of the tokens, check the stack to see what is left.
    # pop it off in that order and add it to the list
    while not opStack.isEmpty():
        post_fix.append(opStack.pop())
    # join the list and return
    return  " ".join(post_fix)


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    # check to see if the operator depends on int order
    def _doMath(op, op1, op2):
        """helper function to compute the two numbers in the stack"""
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2

     # iterate over the list of tokens and check to see if it's a number.
    # if it is, push it to the stack so we can save it for when we find an operator
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            # if it's an operator, pop the first two ints off the stack
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            # do the math necessary per that token
            result = _doMath(token,operand1,operand2)
            # push the result back onto the stack.
            operandStack.push(result)
    # return the last number that is on the stack.
    return operandStack.pop()

print(postfixEval('7 8 + 3 2 + /'))
print(postfixEval('4 5 6 * +'))


print(infix_to_postfix("A * B * C * D + E + F"))
print(infix_to_postfix("A + ( ( B + C ) * ( D + E ) )"))
print(infix_to_postfix("( A + B ) * ( C + D ) * ( E + F )"))
