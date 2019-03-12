from Node import Node


class OrderedList:
    def __init__(self):
        self.head = None

    def is_empty(self) -> bool:
        """Check to see if our ordered list is empty."""
        return self.head is None

    # [1, 2, 3, 8, 12] -> errors when we try to add 4

    def add(self, data: int) -> None:
        """Add a Node to our ordered list."""
        new_node = Node(data) # 1
        stop = False

        # If the list is empty, set the head to the node we are adding
        if self.head is None:
            self.head = new_node
            return

        current = self.head
        previous = None

        while current is not None and not stop:
            if new_node.getData() < current.getData():
                # check to see if there is only one item in the list to also set the head.
                if previous is None:
                    new_node.next = current
                    self.head = new_node
                    stop = True
                else:
                    new_node.next = current
                    stop = True
            else:
                # check to see if it is the end of the list.
                if current.getNext() is None:
                    # check if there is only one item in the list.
                    if previous is None:
                        new_node.next = current
                        stop = True
                    else:
                        previous.next = new_node
                        stop = True
                else:
                    current = current.getNext()
                    previous = current
        print(f"Node: {data} is now in your list.")

    def size(self) -> int:
        """Return the size of our ordered list."""
        current = self.head
        node_count = 0
        while current is not None:
            node_count += 1
            current = current.getNext()
        return node_count

    def search(self, item: int) -> bool:
        """Search our ordered list and return boolean value if item is found."""
        current = self.head
        found = False
        stop = False

        # while there are nodes in the list & the item isn't found & we haven't found a larger int (it's ordered)
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            # if the data we are searching for is larger than the passed in item, it is not in the list
            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found

    def show(self) -> list:
        current = self.head
        lst = []
        while current is not None:
            lst.append(current.getData())
            current = current.getNext()
        return lst

    def remove(self, item: any) -> bool:
        """Removed an item from out ordered list."""
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


myList = OrderedList()
# node_data = [12, 8, 16, 3, 2, 1, 4]

node_data = [12, 8, 16, 3, 2, 1, 4, 88, 22, 31]
prev = None
for data in node_data:
    myList.add(data)
print(myList.size())
print(myList.show())

