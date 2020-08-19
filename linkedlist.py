class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist(Element):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_value):
        current_value = self.head

        if self.head:
            while current_value.next:
                current_value = current_value.next
            current_value.next = new_value
        else:
            self.head = new_value
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        
        counter = 1
        current = self.head
        if position < 1:
            return None
        elif position == 1:
            return current
        else:
            while position >= current:
                if position == current:
                    return current
                current = current.next
                counter += 1

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        counter = 1
        current = self.head

        if position < 1:
            return None
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            while position >= current:
                if counter == position:
                    new_element.next = current
                    current = new_element
                current = current.next
                counter += 1

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.value
        previous = None

        if current.value == value:
            self.head = current.next