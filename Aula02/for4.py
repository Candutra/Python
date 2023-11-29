import os

os.system("clear")

qtd = 0
for tijolo in range(1973,2023):
    if tijolo % 4 == 0:
        qtd = qtd + 1
print("A quantidade de anos bissextos é ")
print(qtd)
    