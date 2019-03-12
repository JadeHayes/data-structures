from Node import Node


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """Check to see if our unordered list is empty."""
        return self.head is None

    def add(self, data: any) -> None:
        """Add a Node to our unordered list."""
        node = Node(data)
        node.setNext(self.head)
        self.head = node
        print(f"Node: {data} is now the head of your list.")

    def size(self) -> int:
        """Return the size of our unordered list."""
        current = self.head
        node_count = 0
        while current is not None:
            node_count += 1
            current = current.getNext()
        return node_count

    def search(self, item: any) -> bool:
        """Search our unordered list and return boolean value if item is found."""
        current = self.head
        found = False

        while current is not None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def append(self, item: any) -> None:
        """Appends an item to the end of our unordered list."""
        current = self.head
        found = False

        while current is not None and not found:
            if current.getNext() is None:
                current.next = Node(item)
                print(f"Node with item: {item} added to the end of our list.")
                found = True
            else:
                current = current.next

    def insert(self, item: any, pos: int) -> None:
        """Inserts a Node at any position in the unordered list."""
        current = self.head
        previous = None
        new_node = Node(item)
        # we are using actual positions, not python index.
        list_position = 1

        if pos > self.size():
            print("Index Error, position out of range.")
            return

        while current is not None:
            if list_position == pos:
                new_node.next = current
                if previous is None:
                    new_node.next = self.head
                    self.head = new_node
                else:
                    previous.next = new_node
                return
            list_position += 1

    def index(self, item: any):
        """Will return the fist index of the Node with data that matches our input item."""
        current = self.head
        index = 0
        previous = None

        while current is not None:
            if current.getData() == item:
                if previous is None:
                    return index
                else:
                    return index
            current = current.getNext()
            index += 1

    def pop(self, index: int = None) -> None:
        """Removes the item from a specific index, defaults to the end of the list."""
        current = self.head
        node_index = 0
        previous = None
        removed = False

        if index is not None and self.size() <= index:
            print("Index error. Given index is out of range.")
            return
        while current is not None and removed is False:
            if current.getNext() is None and index is None:
                print("Popped from the end of the list.")
                previous.next = None

            if index == node_index:
                print(f"Popped from index: {node_index}.")
                if previous is None:
                    self.head = current.getNext()
                else:
                    previous.next = current.getNext()
                removed = True
            else:
                previous = current
                current = current.getNext()
                node_index += 1

    def remove(self, item: any) -> bool:
        """Removed an item from out unordered list."""
        current = self.head
        previous = None
        found = False

        while not found:
            if current is None:
                print(f"Item: {item} not found in the list.")
                return False
            if current.getData() == item:
                print(f"Removing: {current.getData()}")
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous is None:
            self.head.next = current.getNext()
            return True
        elif found is False:
            print(f"Item: {item} not found in the list.")
        else:
            previous.setNext(current.getNext())
            return True


myList = UnorderedList()
node_data = [12, 8, 16, 3, 2, 1, 4, 88, 22, 31]
prev = None
for data in node_data:
    myList.add(data)
print(myList.size())

print(myList.search(2))
print(myList.search(21))
print(myList.search(21))

myList.remove(1)
print(myList.size())
myList.remove(12)
print(myList.size())

# Doesn't exist, should print a message.
myList.remove(120)

myList.append("cherry")
print(myList.size())
myList.insert(4, 2)
myList.insert(5, 1)
print(myList.size())

print(myList.index(4))
print(myList.index(5))

myList.pop(2)
myList.pop()
print(myList.size())


