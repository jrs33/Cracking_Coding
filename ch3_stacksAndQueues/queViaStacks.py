#
# Implement a queue from two stacks
#

class twoStackQueue:

        # Mimicking a Python List as a stack
        # ie:
        #
        #>>> stack = [3, 4, 5]
        #>>> stack.append(6)
        #>>> stack.append(7)
        #>>> stack
        #    [3, 4, 5, 6, 7]
        #>>> stack.pop()
        #7
        #    [3, 4, 5, 6]

    def __init__(self):
        stackOne = List() # Used for adding new elements
        stackTwo = List() # Used for classic FIFO pattern

    def add(self, item):
        if not self.stackOne:
            if not self.stackTwo: # If both are empty, then we just add to the first stack
                self.stackOne.append(item)
            else: # If the second stack is full then we just shuffle back
                self.exchangeStacks()
                self.stackOne.append(item)
        else:
            self.stackOne.append(item)

    def remove(self): # FIFO pattern, so we want to transfer to stackTwo
        if not self.stackTwo:
            if not self.stackOne:
                print("ERROR: EMPTY QUEUE")
            else:
                self.exchangeStacks()
                self.stackTwo.pop()
        else:
            self.stackTwo.pop()

    # Shuffle function used to allow for proper stack to have values for the various
    # queue functions (ie: allows oldest elements to be popped for FIFO pattern)
    def exchangeStacks(self):
        if not self.stackTwo:
            for i in range(len(self.stackOne)):
                self.stackTwo.append(self.stackOne.pop())
        elif not self.stackOne:
            for i in range(len(self.stackTwo)):
                self.stackOne.append(self.stackTwo.pop())

    def isEmpty(self):
        if not self.stackOne and self.stackTwo:
            return True
        else:
            return False
