class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linkedlist(Element):
    def __init__(self, head=None):
        self.head = head

    def add(self, new_value):
        current_value = self.head

        if self.head:
            while current_value.next:
                current_value = current_value.next
            current_value = new_value
        else:
            self.head = new_value

# el1 = Element(1)
# el2 = Element(2)
# li = Linkedlist(3)
# print(li.add(el2))