List=["pen", "pencil", "eraser"]
List2=["book", "notebook", "copybook"]
List3=List+List2
print(List3)

list=[111,222,333]
list2=[444,555,666]
list3=list+list2
print(list3)

list=["a","b","c"]
list2=["d","e","f"]
list3=list+list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
