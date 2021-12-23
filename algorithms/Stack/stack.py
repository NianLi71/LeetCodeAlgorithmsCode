
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[len(self.items) - 1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)


if __name__ == '__main__':
    s = Stack()

    assert s.isEmpty() == True

    s.push(1)
    s.push('a')
    s.push('hello world')
    assert s.size() == 3
    assert str(s) == "[1, 'a', 'hello world']"
    assert s.peek() == 'hello world'

    s.pop()
    print(s)