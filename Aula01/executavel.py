#!/usr/bin/python3
nome = input("Digite o seu nome: ")
anonas = input("Digite o ano do seu nascimento: ")
#Para realizar o calculo da idade foi necessario converter a variavel anonas
#para inteiro, pois o comando imput sempre retorna o valor como texto.
idade = 2023 - int(anonas)
#Para converter o valor numérico em texto, usamos o comando str.
print("Ola sr(a). "+nome+" você tem ou terá este ano: "+str(idade)+" anos")