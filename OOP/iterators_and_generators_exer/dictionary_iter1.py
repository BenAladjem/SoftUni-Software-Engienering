class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.l = len(self.dict.keys())
        self.keys = list(self.dict.keys())
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.l <= self.count:
            raise StopIteration
        key = self.keys[self.count]
        value = self.dict[key]
        self.count += 1
        return key, value

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

