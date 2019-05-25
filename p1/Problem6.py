class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def __str__(self):
        out_string = ""
        for value in self.values():
            out_string += str(value) + " -> "
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            self.size = 1
            return
        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.size += 1

    def values(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def contains(self, value):
        for _value in self.values():
            if value == _value:
                return True
        return False

def union(llist_1, llist_2):
    union = LinkedList()
    for value in llist_1.values():
        if not union.contains(value):
            union.append(value)
    for value in llist_2.values():
        if not union.contains(value):
            union.append(value)
    return union

def intersection(llist_1, llist_2):
    intersection = LinkedList()
    for value in llist_1.values():
        if llist_2.contains(value):
            if not intersection.contains(value):
                intersection.append(value)
    return intersection


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print('List 1:\t\t', linked_list_1)
print('List 2:\t\t', linked_list_2)

print('Union:\t\t', union(linked_list_1,linked_list_2))
print('Intersection:\t', intersection(linked_list_1,linked_list_2))


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print('List 3:\t\t', linked_list_3)
print('List 4:\t\t', linked_list_4)

print('Union:\t\t', union(linked_list_3,linked_list_4))
print('Intersection:\t', intersection(linked_list_3,linked_list_4))