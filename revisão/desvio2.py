# Este algotmos exibe uma mensagem para os motoristas que estão com o seus carros em dias de rodizio

final_placa = input("Digite o numero final da placa do teu carro: ")
# aqui usamos os sinais de comparação, não pra atribuir a valor mas sim em comparar
#se final de placa for semelhante a 1 ou final de placa for semelhante a 2
if(final_placa == "1" or final_placa == "2"):
    print("Seu carro se enquadra na zona de rodizio - Segunda-Feira")
elif(final_placa == "3" or final_placa == "4"):
    print("Seu final de placa esta no dia de rodizio - Terça-Feira")
elif(final_placa == "5" or final_placa == "6"):
    print("Seu final de placa esta no dia de rodizio - Quarta-Feira")
elif(final_placa == "7" or final_placa == "8"):
    print("Seu final de placa esta no dia de rodizio - Quinta-Feira")
elif(final_placa == "9" or final_placa == "0"):
    print("Seu final de placa esta no dia de rodizio - Sexta-Feira")
else:
    print("Final de placa não encontrado :(")

