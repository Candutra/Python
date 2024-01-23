list1 = [1,3,5,9,8]
list2 = [1,2,3,4,5,6,7,8,9]
list3 = [] 



for i in list1:
    for j in list2:
        if i == j:
            list3.append(i)
print("O numero é " +str(list3))

# explicando o codigo:

# list3.append(i) é usado para construir uma lista que contém os elementos que são iguais em ambas as listas list1 e list2


