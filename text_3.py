class Nodes:
    def __init__(self, data):
        self.data = data
        self.next: Nodes = None

class Linkedlists:
    def __init__(self):
        self.head: Nodes = None
        self.tail: Nodes = None

    def insert_head(self, data):
        new_node = Nodes(data)
        new_node.next = self.head
        self.head = new_node

    def insert_tail(self, data):
        new_node = Nodes(data)

        if self.head is None:
            self.head = self.tail = new_node
            return
        
        self.tail.next = new_node
        self.tail = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next

    def insert_where(self, where, data):
        new_node = Nodes(data)
        current = self.head
        while current.data != where:
            current = current.next

        if self.tail.data == where:
            self.tail = new_node
        new_node.next = current.next
        current.next = new_node

    def deletetion(self, where):
        current = self.head
        while current.next.data != where:
            current = current.next

        current.next = current.next.next

    def tell_head_tail(self):
        print("----------------")
        print(f"Head: {self.head.data}")
        print(f"Tail: {self.tail.data}")
        print("----------------")



def linked_list_init():
    llist = Linkedlists()

    for i in range(1, 11):
        llist.insert_tail(i)

    llist.insert_where(5, 5.6)
    llist.insert_where(10, 11)
    llist.insert_where(6, 6.4)
    llist.insert_where(11, 12)

    print("\n")

    llist.traverse()

    print("\n")

    llist.tell_head_tail()

def bitwise_some(i, n ):
    while i < n:
        print(bin(i))
        i += i & (-i) 

b = 10 % (-3)
c = (-10) % 3
a = (-10) % (-3)

print(a)
print(b)
print(c)
