import random
from time import sleep

class Dado:

    def __init__(self):
        self.valor = 1
    
    def iniciar_simulador(self):
        mensagem = '''
        *** Olá seja vem vindo ao meu simulador de dado ***
            o dado será jogado agora, por favor aguarde...\n'''
        print(mensagem)
        sleep(4)
        self.jogar()
        print(f'\nO valor sorteado do dado foi o número {dado.valor}\n')

        self.jogar_novamente()

    def jogar(self):
        self.valor = random.randint(1,6)
        return self.valor

    def jogar_novamente(self):
        while True:
            resposta = input('Gostaria de jogar novamente (s/n)     ')
            if resposta == 'n':
                break
            elif resposta == 's':
                sleep(1)
                print(f'\nO valor sorteado do dado foi o número {self.jogar()}\n')
            else:
                sleep(1)
                print('\nOpa: Houve um erro na sua resposta.\n')
        sleep(1)    
        print('\n*** Obrigado por jogar ***')

dado = Dado()
dado.iniciar_simulador()




