#linked list traversal

class Node:
    """creating a class Node. Node which contains the data and the address"""
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traversal(self):
        if self.head == None:
            print("Linked List is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref

if __name__ == "__main__":
    LL1 = LinkedList()
    LL1.head = Node(1)
    second = Node(2)
    third = Node(3)
    LL1.head.ref = second
    second.ref = third

    LL1.traversal()

