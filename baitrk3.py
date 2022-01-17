

list1 = input("Enter the first list:")
list2 = input("Enter the second list: ")
str = min(len(list1)+ len(list2))
result = [None]*(str*2)
result[::2] = list1[:str]
result[1::2] = list2[:str]
result.extend(list1[str:])
result.extend(list2[str:])
result
print (result)