from que.node import node;
class queue(object):
    def __init__(self, front=None, end=None):
        self.front = front
        self.end = end
    def enqueue(self, data):
        new = node(data)
        if (self.end == None and self.front == None): # if queue is empty to start with
            self.front = new
            self.end = new
        else:
            '''
            current = self.front
            while (current):
                if (current.getNext() == None):
                    current.setNext(new)
                    break;
                else:
                    current = current.getNext()                 
            self.end = current
            '''
            
            self.end.setNext(new)
            self.end = new
            
    def size(self):
        current = self.front
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count
    def display(self):
        current = self.front
        if (current is not None):
            while (current):
                if (current.getNext() != None):
                    print(str(current.getData()) + "->",end='')  
                else:
                    print(str(current.getData()),end='')  
                current = current.getNext() 
            print()
    def dequeue(self):
        current = self.front
        if (current == None): # queue is empty
            #print("queue is empty")
            pass
        elif (current.getNext() == None): # only one node in the queue ...
            self.front = None
            self.end = None
            #print("queue is empty")
        else: # for more than one nodes
            self.front = current.getNext()
            current = None            