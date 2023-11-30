import os

os.system("cls")
print("Temos dois arquivos: bloco_texto.txt e dados.txt")
print("Qual deles você deseja apagar?")
es = input("Digite: \n - 1 para bloco_texto\n - 2 para dado.txt\n")

if es == "1":
    conf1 = input("Você tem certeza que deseja apagar bloco_texto.txt?[s,n]: ")
    if conf1 == "s":
      os.remove("bloco_texto.txt")
      print("Arquivo apagado com sucesso")
    else:
     print("Operação cancelada") 
else:
    conf2 = input("Você tem certeza que deseja apagar dados.txt?[s,n]: ")
    if conf2 == "s":
     os.remove("dados.txt")
     print("Arquivo apagado")
    else:
      print("Operção cancelada")