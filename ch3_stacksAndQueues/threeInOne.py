#
# Using a single array to implement three stacks
#

class triStack(object):
    '''
    Class that contains three fixed size stacks from a single array
    '''

    class Node:
        data = None
        next = None

        def __init__(self, data):
            self.data = data

    def __init__(self, size):

        topArray = [None for i in range(size)]
        inputArray = [Node.__init__(None) for i in range(size)]

        for i in range(0, len(inputArray), 3):
            # yield is a keyword that is used like return, except the function will return a generator
            # and we use it in this case to split up the array into 3 even chunks
            yield inputArray[i:i + 3]

    def pop(self, numStack):
        if(self.topArray[numStack] == None):
            print("ERROR: EMPTY STACK")
        else:
            self.top[numStack]

    def push(self, data, numStack):
        node = self.Node.__init__(data)
        node.next = self.topArray[numStack]

        self.inputArray[numStack].push(node)
        self.topArray[numStack] = data

    def peek(self, numStack):
        if(self.topArray[numStack] == None):
            print("ERROR: EMPTY STACK")
        else:
            return topArray[numStack]

    def isEmpty(self, numStack):
        self.topArray[numStack] == None

# As you can see, this is a simple stack implementation with an addition
# of an topArray to track top values for each of the three stacks. The downside
# here is that the stacks are fixed size
