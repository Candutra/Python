from class_client import cliente

nome = input("Digite o nome do Cliente: ")
email = input("Digite o email do Cliente: ")
cpf = input("Digite o cpf do Cliente: ")
idade = input("Digite o idade do Cliente: ")
telefone = input("Digite o telefone do Cliente: ")

# Vamos instanciar a classe cliente. Gerar um objeto
# a partir da classe Cliente passando todas as
# propriedades para o objeto criado
cli = cliente()
cli.gravarCliente(nome,email,cpf,idade,telefone,)