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
        return None
