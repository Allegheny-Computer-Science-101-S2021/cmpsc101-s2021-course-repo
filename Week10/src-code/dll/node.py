class node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
    def getData(self):
        return self.data
    def getPrev(self):
        return self.prev
    def setPrev(self, new):
        self.prev = new
    def getNext(self):
        return self.next
    def setNext(self, new):
        self.next = new