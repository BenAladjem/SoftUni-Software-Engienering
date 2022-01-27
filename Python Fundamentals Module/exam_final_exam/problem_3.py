text = input()
key_words = input().split(" | ")
command = input()

words = text.split(" | ")
my_dict = {}
my_list1 = []
my_list2 = []
a = []
b = []
for word in words:
    d = word.split(": ")
    key = d[0]
    my_list1.append(key)
    value = d[1]
    my_list2.append(value)
    my_dict[key] = value
#print(my_dict)
ind = 0
if command == "Test":
    l1 = my_list1[::-1]
    l2 = my_list2[::-1]
    for k in key_words:
        if k in l1:
            print(f"{k}:")
            #l1 = my_list1[::-1]
            ind  +=0
            for m in l1:
                if k == m:

                    poss_k = l1.index(m)
                    a.append(l2[poss_k])
                    for c in a:
                        b.append(len(c))
                    #print(a)
                    #print(b)
                    if len(a)>1:
                        if b[0]< b[1]:
                            print(f" -{a[0]}")
                        else:
                            print(f" -{a[1]}")
                    else:
                        print(f" -{a[0]}")
                    l1[poss_k] = "rrr"


elif command == "Hand Over":
    my_dict = (sorted(my_dict.items(), key = lambda x:x[0]))
    for key,value in my_dict:
        print(f"{key}",end=' ')