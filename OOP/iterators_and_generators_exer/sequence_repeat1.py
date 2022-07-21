class sequence_repeat:
    def __init__(self, word, num):
        self.word = word
        self.num = num
        self.count = 0
        self.l = len(word)
        self.index = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.num:
            raise StopIteration
        res = self.word[self.index]


        self.count += 1
        self.index += 1
        if self.count >= self.l:
            self.index = self.count % self.l

        return res

result = sequence_repeat('abc', 8)
for item in result:
    print(item, end='')