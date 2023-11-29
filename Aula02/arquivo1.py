# importar a blibioteca os(sistema operacional)
import os

#Limpar a tela
os.system("clear")

arq = open("./texto.txt","w")
arq.write("Hoje é quarta-feira\nÚltima semana de novembro")
arq.close()