import struct

imei = 865456053906614
word = 'text'
number = 123.141516223344
protocol = b'U\xaa\x1d\x03\x13 \xb0\xa9l\xb6\x01\x00\xd8\x01\x027\xa1\x00\xde\x01\x017\x00\xd2\x01\x01(\x9dn'
'''
>>> aa = "ABC"
>>> bb = aa.encode()
>>> bb
b'ABC'
>>> cc =bb.decode('utf-8')
>>> cc
'ABC'
>>> type(aa)
<class 'str'>
>>> type(bb)
<class 'bytes'>
>>> type(cc)
<class 'str'>
>>> 
'''
#struct.pack('B',val)/ struct.unpack('B',val)
def ByteToHex(byteStr):
    # Служи за отпечатване на byte array в удобен за възприемане вид
    return " ".join(["{:02x}".format(x) for x in byteStr])


def dec_hex_byte(value, num_bytes):

    res = (value).to_bytes(num_bytes, byteorder='big')
    return res

def float_to_bytearray(f):
    # Convert float number to bytearray
    return struct.pack(f)

def bytearray_to_float(n):
    # Convert bytearray to float
    return float(struct.unpack("=d", n)[0])


#  4240.4864,N,02317.3875,E
gps  = {'N':4240.4864,'E':02317.3875,}
n = 42.404864
e = 023.173875
f = struct.pack(">f", number) # for float codding
ff = float(struct.unpack(">f", f)[0])  # Връща тюпъл
print(f"n={n}")
nn = struct.pack("=d", n)
print(f"nn={nn}")
nx = float(struct.unpack("=d", nn)[0])
print(f"nx={nx}")
print()
print(f"e={e}")
ee = struct.pack("=d", e)
print(f"ee={ee}")
ex = float(struct.unpack("=d", ee)[0])
print(f"ex={ex}")

#print(f"ff={ff}")
#a = word.encode()
#print(a)
#print(f"num={f}")
#print(ff)
#x = float(f"{ff:.4f}")
#print(f"x={x}")
#print(f"{ff:.4f}")
#print(ByteToHex(f))
#b = a + f + protocol
#print(b)
#print(ByteToHex(a))
#print(ByteToHex(b))