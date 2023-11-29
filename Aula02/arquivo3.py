import os

os.system("clear")

arq = open("./Arquivos/info.csv","r")
print(arq.read())
arq.close()