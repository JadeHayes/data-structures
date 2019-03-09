# A queue is an ordered collection of items where the addition of new items happens at one
# end, called the “rear,” and the removal of existing items occurs at the other end, commonly called the “front.”

# FIFO, first-in first-out


# This class assumes the rear is at position 0, which is the opposite how how a python list works.
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
q.isEmpty()
q.enqueue("puppy")
q.enqueue(True)
q.enqueue(8)
q.enqueue("pop_me")
q.dequeue()
q.isEmpty()
q.size()