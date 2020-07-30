import random

list1 = random.sample(range(100),10)
list2 = random.sample(range(100),10)
list3 = []
for k in range(10):
    list3.append(list1[k])
    list3.append(list2[k])

print("Lista 1: ",list1)
print("Lista 2: ",list2)
print("Lista Alternada: ",list3)
