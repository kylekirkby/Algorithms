class Stack:

    """This is the class for a stack data structure"""

    def __init__(self,max_size):

        self.items = []
        self.max_size = max_size
        self.stack_pointer = 0

    def size(self):

        length = len(self.items)

        return length

    def push(self, item):

        size = self.size()
        
        if self.max_size > size:

            self.items.append(item)
            self.stack_pointer = size
            return True
        
        else:
            
            print("Stack is full.")
            return False

    def pop(self):

        size = self.size()
        if size != 0:
            self.items.pop()
            self.stack_pointer = size
            return True
        else:
            print("Stack is empty.")
            return False

    def peek(self):
        empty = self.is_empty()
        if empty == True:
            print("Stack is empty.")
        else:    
            lastItem = self.items[-1]
            return lastItem
            
            
    def is_empty(self):

        if len(self.items) == 0:
            return True
        else:
            return False
        

def main():
    stack = Stack(5)
    print(stack.items)
    print(stack.stack_pointer)
    print(stack.peek())
    for i in range(1,10):
        stack.push(i)
        print(stack.items)
    for i in range(1,10):
        stack.pop()

    print(stack.is_empty())
        

if __name__ == "__main__":

    main()
