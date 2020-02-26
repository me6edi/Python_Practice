#author Mahmud Ahsan
#-------------------------------
#         Tuple
#-------------------------------

#Comparing
t1 = 1, 2, 3
t2 = 1, 3, 2
if t1 == t2:
    print("t1 and t2 values are equal")
tp = 1, 2, 'bill', 4.4, False
print(tp,type(tp))

# Immutable
t1 = 'Bill' , 2, 3
t1 = 1, 2, 3
print(t1)

t1 = 5, 7, 11
x, y, _ = t1
print(x, y, _, sep = ' | ')

# Syntx

""""
dict = {
key : value
}
"""
# dict = {}
# # print(dict, type(dict))
# dict ['name'] = 'Swift'
# dict['age'] = 55
# dict[55] = 555
# print(dict['name'], '|', dict[age], '|', dict[55])

dict = {'bill' : '01235466740', 'steve' : '012434264'}
print(dict['bill'])
print(dict['steve'])
print(len(dict))

# Modification
shop_items_price_kg = {'price' : 44, 'flour' : 33}
print(shop_items_price_kg)


asci_dict = {'a':97, 'b':98, 'c':99, 'd':100}
for key, value in asci_dict.items():
    print(key, value, sep='->')

# shop_items_price_kg ={
#     'rice' :44,
#     'flour': 33,
#     'oil': 32
# }
# print(shop_items_price_kg)
# for key in shorted(shop_items_price_kg.keys()):
#     print(key,shop_items_price_kg[key])
