import json

def ByteToHex(byteStr):
    # Служи за отпечатване на byte array в удобен за възприемане вид
    return " ".join(["{:02x}".format(x) for x in byteStr])

nums = [3, 2, 44, 56, 61, 4]
filename = 'nums.json'
with open(filename, 'w') as f:
    json.dump(nums, f)

file1 = 'nums.json'
with open(file1) as fl:
    nums_new = json.load(fl)

"""
data = {
  "response":{
    "count": 1234567,
    "items":[{
        "First name": "Tom",
        "ID": 123456,
        "Last name": "Krus"
    },{
        "First name": "Ben",
        "ID": 987654,
        "Last name": "Aladjem"
    }]
}
}
"""
print(nums_new)
print(type(nums_new))

x = json.dumps(nums)
print(x)
print(type(x))
y = x.encode()
print(y)
print(type(y))
print(ByteToHex(y))