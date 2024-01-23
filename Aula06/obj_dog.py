from classe_dog import Dog

# Para criar o objeto, utilizamos a variavel pastor e realizamos o processo de instanciação da classe 'dog
# Foi passado o nome e a idade do cachorro  
pastor = Dog("Bob",6)
# Acessamos o metodo data_dog que mostra os dados  do cachorro
pastor.data_dog()
pastor.sit()
pastor.roll_over()
print(pastor.__class__)
print(pastor.__dict__)