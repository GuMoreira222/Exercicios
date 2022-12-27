from lib import interface
from lib import arquivo
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)
while True:
    opcoes = ['Ver pessoas cadastradas', 'Cadastrar uma pessoa', 'Sair do sistema']
    opcao = interface.menu(opcoes)
    if opcao == 1:
        arquivo.lerArquivo(arq)
        sleep(2)
    elif opcao == 2:
        interface.cab("CADASTRAR UMA PESSOA")
        nome = input("Nome: ")
        idade = interface.leiaint("Idade: ")
        arquivo.cadastrar(arq, nome, idade)
        sleep(2)
    elif opcao == 3:
        interface.cab("Finalizando sistema... Até logo!")
        sleep(2)
        break
    else:
        print("\033[31mERRO! Digite uma opção válida.\033[m")
        sleep(2)


