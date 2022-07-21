class sequence_repeat:
    def __init__(self, text, num):
        self.text = text
        self.num = num
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.num ==0:
            raise StopIteration
        ch = self.text[self.idx]
        self.num -= 1
        self.idx +=1
        if self.idx >= len(self.text):
            self.idx = 0
        return ch






result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')