# what distinguishes one linear structure from another is the
# way in which items are added and removed, in particular the location where these additions and removals occur.

# Stack (like a stack of pancakes) items are removed from the top and added from the top
#  Items stored at the base of the stack are there the longest. The most recently placed
# Item is moved first. LIFO last-in-first-out.  Newer items are at the top and older items
# are at the base. The order items are removed is exactly the reverse of the order that they were placed.
# Stacks can be used to reverse the order of items.  The order of insertion is reverse the order of removal

# ex: web browser back button, (as you navigate URL's get stored in a Stack)

#  Stack operations are:
# - push(item)
# - pop()
# - peek()
# - isEmpty()
# - size()


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item: any):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

stack = Stack()
print(stack.is_empty())
stack.push("puppy")
stack.push("tommy")
stack.push(8)
stack.push(True)
print(stack.peek())
print(stack.size())
stack.pop()
print(stack.is_empty())


def revstring(mystr: str):
    stack = Stack()
    ans = ""

    for letter in mystr:
        stack.push(letter)

    while not stack.is_empty():
        ans += stack.pop()
    print(ans)

revstring("banana")

