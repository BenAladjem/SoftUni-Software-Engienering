imei = 865456053906614
imei_b_arr = imei.to_bytes(7, byteorder='big')
imei_hex = hex(imei)[2:]

def ByteToHex(byteStr):
    return " ".join(["{:02x}".format(x) for x in byteStr])


a = (865456053906614).to_bytes(7, byteorder='big')
print(ByteToHex(a))
data = 142415
def to_bytes_without_len(d):
    # Convert int to bytearray / unknown num of bytes, returns bytearray
    count = 0
    res = (d).to_bytes(7, 'big')
    print(res[0])
    for i in range(7):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return result

def to_bytes_and_len(d):
    # Convert int to bytearray / returns num of bytes
    count = 0
    res = (d).to_bytes(7, 'big')
    print(res[0])
    for i in range(7):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return count


print(ByteToHex(to_bytes_without_len(data)))