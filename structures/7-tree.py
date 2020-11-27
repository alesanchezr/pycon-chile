from _utils import PrintableBTree

class Tree(PrintableBTree):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.value = data
    def insert(self, data):
        if self.value:
            if data < self.value:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.value:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.value = data



root = Tree(20)
root.insert(11)
root.insert(25)
root.insert(10)
root.insert(30)
root.insert(19)
root.display()








