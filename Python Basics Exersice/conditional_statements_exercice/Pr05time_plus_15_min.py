hour = int(input())
min = int(input())


def minut(m):
    result = ""
    if m <10:
        result = "0"+str(m)
    else:
        result = str(m)
    return  result


def houre(h):
    result = ""
    if h>23:
        result = "0"
    else:
        result = str(h)
    return result


time = hour*60 + min + 15
h_result = time//60
m_result = time - h_result*60
print(houre(h_result)+":"+minut(m_result))




