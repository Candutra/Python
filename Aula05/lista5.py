import os

os.system("clear")

n1 = [11,23,42,41,56,463,12,78,21]
n2 = [12,42,32,56,54,63,75,78,463,324,21,43,34,53,28]
n3 = []
n4 = []

for i in n1:
    for j in n2:
        if i == j:
            # print(i)
            n3.append(i)
        if i % j == 0:
            n4.append(i)

print(n3)
print(n4)