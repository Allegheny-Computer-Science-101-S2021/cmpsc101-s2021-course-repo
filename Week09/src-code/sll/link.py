from node import node;
class link(object):
    def __init__(self, head=None):
        self.head = head
    def insert(self, data):
        new = node(data)
        new.setNext(self.head)
        self.head = new
    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
            return count
    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
            if current is None:
                raise ValueError("Data not in list")
        return current
    def display(self):
        current = self.head
        while (current):
            if (current.getNext() != None):
                print(str(current.getData()) + "->",end='')  
            else:
                print(str(current.getData()),end='')  
            current = current.getNext() 
        print()
    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getNext()
            if current is None:
                raise ValueError("Data not in list")
            if previous is None and found:
                self.head = current.getNext()
            elif previous is not None and found:
                previous.setNext(current.getNext())
