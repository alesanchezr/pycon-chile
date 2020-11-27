class Stack:
    _list = []
    def push(self,value):
        print("Pushing ",value)
        self._list.append(value)

    def pop(self):
        print("Poping the first one on the stack")
        self._list.pop()
    
    def print(self):
        print("This is the current stack: ",self._list)


all_cards = Stack()
all_cards.push('2♦️')
all_cards.push('5♥️')
all_cards.push('6♣️')
all_cards.print()
all_cards.pop()
all_cards.print()