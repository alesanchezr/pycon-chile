class Stack:
    _list = []
    def enque(self,value):
        print("Enqueue ",value)
        self._list.append(value)

    def dequeue(self):
        print("Poping the first one that came in")
        self._list.pop(0)
    
    def print(self):
        print("This is the current stack: ",self._list)


all_cards = Stack()
all_cards.enque('Tom')
all_cards.enque('Maria')
all_cards.enque('Allie')
all_cards.print()
all_cards.dequeue()
all_cards.print()