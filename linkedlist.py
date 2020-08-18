class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist(Element):
    def __init__(self, head):
        self.head = head

    def add(self, new_value):
        current_value = self.head

        if self.head:
            while current_value:
                current_value = current_value.next
            current_value.append(new_value)
        else:
            self.head = new_value
        