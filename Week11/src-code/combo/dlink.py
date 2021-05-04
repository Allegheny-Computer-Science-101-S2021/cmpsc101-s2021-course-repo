from dnode import dnode;
class dlink(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
    def insertF(self, data):
        new = dnode(data)
        new.setNext(self.head)
        if (self.head is not None):
            self.head.setPrev(new)
        else:
            self.tail = new
        self.head = new
    def insertE(self, data):
        new = dnode(data)
        if (self.tail is not None):
            self.tail.setNext(new)
            new.setPrev(self.tail)
        else:
            self.head = new
        self.tail = new                 
    
    def insertP(self, pos, data):
        new = dnode(data)
        if (self.head == None): # if linked list is empty to start with
            self.head = new
            self.tail = new
        else:
            current = self.head
            if (pos == 0):
                new.setNext(self.head)
                self.head.setPrev(new)
                self.head = new
            else:
                temp = 0
                while (temp < pos-1): # iterate till pos-1
                    current = current.getNext()  
                    temp += 1
                new.setNext(current.getNext())
                if current.getNext() is not None: # for all nodes except last node
                    current.getNext().setPrev(new)
                else: # last node 
                    self.tail = new
                current.setNext(new)
                new.setPrev(current)
    

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count
    def searchF(self, data):
        current = self.head
        found = False
        pos = 0
        while current and found is False:
            if current.getData() == data:
                found = True
            else:
                current = current.getNext()
                pos += 1
            if current is None:
                return -1
        return pos
    def displayF(self):
        current = self.head
        while (current):
            if (current.getNext() != None):
                print(str(current.getData()) + "<->",end='')  
            else:
                print(str(current.getData()),end='')  
            current = current.getNext() 
        print()
    def displayR(self):
        current = self.tail
        while (current):
            if (current.getPrev() != None):
                print(str(current.getData()) + "<->",end='')  
            else:
                print(str(current.getData()),end='')  
            current = current.getPrev() 
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
           
            if current is self.head and found:
                self.head = current.getNext()
                if current.getNext() is not None:
                    current.getNext().setPrev(None)
                if (current is self.tail): # both head and tail, that is there is only one node. 
                    self.tail = current.getPrev()
                current = None
            elif current is self.tail and found:
                previous.setNext(None)
                self.tail = previous
                current = None
            elif previous is not None and found:
                previous.setNext(current.getNext())
                current.getNext().setPrev(previous)
                current = None