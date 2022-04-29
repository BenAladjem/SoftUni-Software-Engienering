data = [{'id': 216, 'value': 14241, 'type': 1}, {'id': 222, 'value': 55, 'type': 1}, {'id': 210, 'value': 40, 'type': 1}]
#data  = [{'id': 216, 'value': 14241, 'type': 1}]

def ByteToHex(byteStr):
    # Служи за отпечатване на byte array в удобен за възприемане вид
    return " ".join(["{:02x}".format(x) for x in byteStr])

def dec_hex_byte(value, num_bytes):

    res = (value).to_bytes(num_bytes, byteorder='big')
    return res

def to_bytes_without_len(d):
    # Convert int to bytearray / unknown num of bytes, returns bytearray
    count = 0
    res = (d).to_bytes(7, 'big')
    #print(res[0])
    for i in range(7):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return result

def to_bytes_and_len(d):
    # Convert int to bytearray / returns num of bytes
    count = 0
    res = (d).to_bytes(10, 'big')
    #print(res[0])
    for i in range(10):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return count

def data_convert(d):

    res = b''
    for i in d:
        print(i)
        d_type_id = dec_hex_byte(i["id"], 2)
        d_type = dec_hex_byte(i["type"], 1)
        d_value = to_bytes_without_len(i["value"])
        d_length = dec_hex_byte(to_bytes_and_len(i["value"]), 1)
        res += (d_type_id+d_type+d_length+d_value)

        print(f"data type ID={d_type_id}")
        print(f"data type={d_type}")
        print(f"data length={d_length}")
        print(f"value={d_value}")

    return res

print(data_convert(data))
