#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        Running time: O(n) because it always has to traverse the n amount of nodes"""
        # TODO: Loop through all nodes and count one for each
        length = 0
        current_node = self.head
        if not self.is_empty():
            length += 1
            while current_node.next is not None:
                current_node = current_node.next
                length += 1
        return length

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        Running time: O(1) it's always constant time because you are just
        placing a new node at the already known end of the linked list"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        current_node = self.tail
        # Check if linked list is not empty
        if not self.is_empty():
            current_node.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        Running time: O(1) it's always constant time because you're just
        placing a new node at the start of the linked list"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        current_node = self.head
        # Check if linked list is not empty
        if not self.is_empty():
            new_node.next = current_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node



    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        Best case running time: O(1) best case is if it's found at the first node
        Worst case running time: O(n) worst case if it has to traverse the
        entirety of the linked list or if it's not found"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current_node = self.head

        while current_node is not None:
            if quality(current_node.data):
                return current_node.data
            else:
                current_node = current_node.next
        return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) if the item we're looking for is the first node
        Worst case running time: O(n) if it's the last node in the linked lists
        or if it isn't found"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))

        previous_node = None
        current_node = self.head

        while current_node is not None:
            if current_node.data == item:
                if current_node == self.head and current_node == self.tail:
                    self.head = None
                    self.tail = None
                elif current_node == self.head:
                    self.head = current_node.next
                    current_node.next = None
                elif current_node == self.tail:
                    previous_node.next = None
                    self.tail = previous_node
                else:
                    previous_node.next = current_node.next
                    current_node.next = None
                return
            else:
                previous_node = current_node
                current_node = current_node.next

        raise ValueError('Item not found: {}'.format(item))



def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
