#QUEUES AND DEQUEUES

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)

q = Queue()
print(q.isEmpty())
q.enqueue(1.5)
q.enqueue(1)
q.enqueue(3.75)
q.enqueue(5.24)
q.enqueue(6)
q.enqueue(10.1)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()