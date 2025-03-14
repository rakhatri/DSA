from debugpy.common.timestamp import current


class Node:
    """
    An object for storing a single node of a linked list.
    Models two attributes - data and link to the next node in the list
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return "<Node data: %s>" % self.data


class LinkedList:
    """
    Singly Linked List
    """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Return the number of nodes in the list.
        Takes O(n) time
        """
        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node

        return count

    def add(self, data):
        """
        Adds a new node containing data at the head of the list.
        Takes O(1) time
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Takes O(n) time
        """
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self, data, index):
        """
        Inserts a new node at index position
        Insertion take O(1) time but finding the node at the insertion point takes O(n) time.
        Takes overall O(n) time
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1

            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self, key):
        """
        Removes Node containing data that matches the key
        Returns the node or None if key doesn't exist
        Takes O(n) time
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node

        return current

    def remove_by_index(self, index):
        current = self.head

        if index == 0:
            self.head = current.next_node
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1

        prev_node = current
        current = current.next_node
        next_node = current.next_node
        prev_node.next_node = next_node
        return current

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head
        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            current = current.next_node
        return '-> '.join(nodes)

# N1 = Node(10)
# print(N1)
# N2 = Node(20)
# print(N2)
# N1.next_node = N2
# print(N1.next_node)


# l = LinkedList()
# N1 = Node(10)
# l.head = N1
# print(l.size())

l = LinkedList()
l.add(1)
print(l.size())
l.add(2)
l.add(3)
print(l.size())
print(l)
n = l.search(3)
print(n)
l.insert(10, 1)
print(l)
x = l.remove(2)
print(x)
print(l)
l.add(11)
l.add(12)
print(l)
l.remove_by_index(2)
print(l)

