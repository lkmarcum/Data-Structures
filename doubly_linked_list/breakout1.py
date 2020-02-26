class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add(self, value):
        self.next = Node(value)


node1 = Node(1)
node1.add(2)
node2 = node1.next
node2.add(3)
node3 = node2.next
node3.add(4)
node4 = node3.next
node4.add(5)
node5 = node4.next
node5.add(6)
node6 = node5.next
node6.add(7)

# How do you find and return the middle node of a singly linked list in one pass? You do not have access to the length
# of the list. If the list is even, you should return the first of the two “middle” nodes. You may not store the nodes
# in another data structure.


def find_middle_node(node):
    node_a = node
    node_b = node
    while node_b.next is not None and node_b.next.next is not None:
        node_a = node_a.next
        node_b = node_b.next.next
    return node_a.value


def reverse_list(node):
    cursor_one = node
    cursor_two = node.next

    while cursor_two is not None:
        cursor_two.next = cursor_one

        if cursor_one == node:
            cursor_one = None

        cursor_two = cursor_two.next
        cursor_one = cursor_one.next
