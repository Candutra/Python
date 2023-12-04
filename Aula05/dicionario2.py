import os

os.system("clear")

capitais = {
    "Acre" : "Rio Branco",
    "Alagoas" : "Maceió",
    "Amapá" : "Macapá",
    "Amazonas" : "Manaus",
    "Bahia" : "salvador",
    "Ceará" : "Fortaleza",
    "Espirito Santo":"Vitoria",
    "Goiás":"Goiâna",
    "Maranhão":"São Luis",
    "Mato Grosso":"Cuiabá",
    "Mato Grosso do Sul":"Campo Grande",
    "Minas Gerais":"Belo Horizonte",
    "Pará":"Belém",
    "Paraiba":"João Pessoa",
    "Paraná":"Curitiba",
    "Pernambuco":"Recife",
    "Piauí":"Teresina",
    "Rio Grande do Sul":"Porto Alegre",
    "Rondônia":"Porto Velho",
    "Roraima":"Boa Vista",
    "Santa Catarina":"Florianópolis",
    "São Paulo":"São Paulo",
    "Sergipe":"Aracaju",
    "Tocantins":"Palmas",
    "Distrito Federal":"Brasilia",
    }

# for i in capitais:
#         print(i)

# print(capitais[0:6])
# print(capitais["Acre"])
# Pegar os 6 primeiros itens
ps = 1
for i in capitais:
    if ps < 6:
        print("a capital de "+i+" é "+capitais[i])
    else:
        break
    ps=ps+1