from stack.node import node;
class stack(object):
    def __init__(self, top=None, bottom=None):
        self.top = top
        self.bottom = bottom
    def push(self, data):
        new = node(data)
        if (self.bottom == None and self.top == None): # if stack is empty to start with
            self.bottom = new
            self.top = new
        else:
            '''
            current = self.bottom
            while (current):
                if (current.getNext() == None):
                    current.setNext(new)
                    break;
                else:
                    current = current.getNext()                 
            self.top = new
            '''
            # approach 2 implementation of push
            self.top.setNext(new)
            self.top = new
            
    def size(self):
        current = self.bottom
        count = 0
        while current:
            count += 1
            current = current.getNext()
        return count
    def display(self):
        current = self.bottom
        if (current is not None):
            while (current):
                if (current.getNext() != None):
                    print(str(current.getData()) + "->",end='')  
                else:
                    print(str(current.getData()),end='')  
                current = current.getNext() 
            print()
    def pop(self):
        current = self.bottom
        if (current == None): # stack is empty
            print("stack is empty")
        elif (current.getNext() == None): # only one node in the stack 
            self.bottom = None
            self.top = None
            #print("at this point, you had deleted all elements in the stack")
        else:
            while (current):
                    if (current.getNext().getNext() == None):
                        current.setNext(None)
                        break;
                    else:
                        current = current.getNext()                 
            self.top = current

