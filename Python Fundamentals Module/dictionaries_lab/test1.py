my_dict = {'Peter':21, 'George': 18, 'John':45}
#print(my_dict)

#print(sorted(my_dict.items(), key = lambda x:x[0]))#сортира по ключове
#print(sorted(my_dict.items(), key = lambda x:x[1], reverse=True))#сортира по стойности

#for key, value in sorted()
d = {'Audi A6': ['38000', 62],\
     'Mercedes CLS': ['11000', '35'],\
     'Volkswagen Passat CC': ['45678', '5']}
# print(d["Mercedes CLS"][0])
#
# for key,value in d.items():
#      print(f"{key}, <=> {value}")
# print('Audi A6' in d.keys())
print(sorted(d.items(), key= lambda x:x[1][0],reverse=False))