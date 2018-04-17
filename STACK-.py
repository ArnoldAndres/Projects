class Stack:
    def __init__(self):
        self.items = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def duplicate(self):
        return duplicate(self.items)


if __name__ == "__main__":
    s = Stack()
    x = 0
    while x <= 100:
        s.push(x)
        print (s.peek())
        x += 1

    Stack = input("ENTER NUMBERS: ")
    Stack = list(Stack)
    s = []

    for i in Stack:
        if i not in s:
            s.append(i)

    print (s)