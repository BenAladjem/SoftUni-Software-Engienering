class dictionary_iter:
    def __init__(self, dict):
        self.dict = dict
        self.keys = list(self.dict.keys())
        self.keys_idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.keys_idx >= len(self.keys):
            raise StopIteration
        key = self.keys[self.keys_idx]
        value = self.dict[key]
        self.keys_idx +=1
        return key, value


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)