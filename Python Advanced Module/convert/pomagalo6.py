# Проверка за тип на данните

data = [{'id': 216, 'value': 14241, 'type': 1}, {'id': 222, 'value': '**string # value**', 'type': 2}, {'id': 210, 'value': 40, 'type': 1}]

def check_type_value(v):
    #Проверявя типа на данните и връща резултат, който отговаря на типа
    type_v = type(v)
    if type_v == int:
        res = 1
    elif type_v == str:
        res = 2
    elif type_v == float:
        res = 3
    else:
        res = 4
    return res


'''
Convert int to bytearray / unknown num of bytes, returns bytearray
'''
def to_bytes_without_len(d):
    count = 0
    res = (d).to_bytes(10, 'big')
    for i in range(10):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return result


'''
Convert int to bytearray / returns num of bytes
'''
def to_bytes_and_len(d):
    count = 0
    res = (d).to_bytes(10, 'big')
    for i in range(10):
        if res[i] != 0:
            count += 1
    result = (d).to_bytes(count, 'big')
    return count


'''
Convert int to byte array
'''
def dec_hex_byte(value, num_bytes):
    res = (value).to_bytes(num_bytes, byteorder='big')
    return res


def string_to_bytearray(st):
    # Writes string data and returns bytearray
    res = st.encode()
    return res


def data_convert(d):
    #Чете масива DATA, като съединявя всички речници подред в byte array
    res = b''
    for i in data:
        v = i['value']
        #res = b''
        print(check_type_value(v))
        if check_type_value(v) == 1:
            d_type_id = dec_hex_byte(i["id"], 2)
            d_type = dec_hex_byte(i["type"], 1)
            d_value = to_bytes_without_len(i["value"])
            d_length = dec_hex_byte(to_bytes_and_len(i["value"]), 1)
        elif check_type_value(v) == 2:
            d_type_id = dec_hex_byte(i["id"], 2)
            d_type = dec_hex_byte(2, 1)
            d_value = string_to_bytearray(i["value"])
            d_length = dec_hex_byte(len(d_value), 1)
        elif check_type_value(v) == 3:
            pass
        else:
            pass
        res += (d_type_id + d_type + d_length + d_value)
        #print(res)

    return res

def bytearray_to_str(d):
    # Uncodding bytearray, returns string
    res = d.decode('utf-8')
    return res


print(data_convert(data))