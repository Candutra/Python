# Declaração da classe cliente. Esta classe permite que sejam criados novos objetos do tipo cliente 


class Cliente:
    # A implementação do metodo __init__ representa a construção do metodo construtor da classe, responsavel por inicializar o objeto que será criado. Este metodo possui um argumento self que que faz refenecia a propria classe. Quando for criar uma classe deve-se utilizar o comando self para refenciar a propria classe a qual pertence 
    # Note que o metodo __init__ (Construtor) foram iniciados os atributos da classe, representado as caracteristicas do cliente todos eles foram criador usando o comando self, que indica que eles pertencem a classe Cliente. Os atributos foram declarados como privados. Para isso utilizamos 2 undescores (__)
    # O termo self é uma convenção usada em algumas linguagens de programação, como Python, para se referir ao próprio objeto dentro de uma classe. Self é como uma palavra especial que significa "este carro específico". Então, quando você diz self.valor ou self.imprimir_valor(), você está basicamente dizendo "o valor deste carro específico" ou "imprimir o valor deste carro específico".
    
    '''A classe cliente gera novos cliente e pede alguns dados pessoais e é capaz que salvar o cliente'''
    def __init__(self):
        self.__nome = ""
        self.__idade = 0
        self.__genero = ""
        self.__email = ""
    
    # O metodo gravar exibe uma menssagem com o nome do cliente dizendo q foi salvo com sucesso
    def gravar(self):
        print("O cliente " +self.__nome+ " foi gravado com sucesso")
        ''' 
            O metodo gravar exibe uma mensagem com o nome do cliente e gravação realizada com sucesso 
        '''

    # O metodo dados é utilizado para realizar a passagem dos dados do cliente para dentro da classe Cliente 
    def dados(self,nome = "",idade = 0,genero = "",email= ""):
        ''' 
         O metodo dados pede algumas informações do cliente para que ele seja salvo no sistema
        '''
        self.__nome = nome
        self.__idade = idade
        self.__genero = genero
        self.__email = email


# def 
        # dados colocar os dados do cliente no class 
        # delf grava grava os dados
 


      
