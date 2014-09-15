class Node:
    """Class for the node object in the linked lists"""

    def __init__(self, data):

        self.data = data
        self.nextPointer = None

    def setData(self,data):
        self.data = data

    def setNextPointer(self, data):
        self.nextPointer = data
                                
    def getData(self):
        return self.data

    def getNextPointer(self):
        return self.nextPointer

    
class UnorderedList:

    """ Unordered List"""

    def __init__(self):

        self.head = None

    def isEmpty(self):

        return self.head == None

    def add(self, data):
        
        temp = Node(data)
        temp.setNextPointer(self.head)
        self.head = temp
    
    def getList(self):
        current = self.head
        nextPoi
        
        while current.getNextPointer() != None:
            
            
            

    def length(self):
        pass

    def search(self):
        pass

    def remove(self):
        pass

class OrderedList(UnorderedList):

    """ Ordered List"""

    def __init__(self):

        super().__init__()

    def search(self):
        pass

    def add(self):
        pass



