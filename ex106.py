from time import sleep

c = ('\033[m',
    '\033[7;40m',
    '\033[30;42m',
    '\033[30;44m')

def pyhelp(com):
    titulo(f"ACESSANDO O MANUAL DO COMANDO '{comando}'", 3)
    print(c[1], end='')
    help(com)
    print(c[0], end='')
    sleep(2)
      
def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print("="*tam)
    print(f"  {msg}  ")
    print("="*tam)
    print(c[0], end='')
    sleep(2)

while True:
    titulo("SISTEMA DE AJUDA PyHELP", 2)
    comando = input("Função ou Biblioteca > ")
    if comando.upper() == 'FIM':
        break
    else:
        pyhelp(comando)
print("FINALIZANDO...")
sleep(2)
titulo("<< ATÉ LOGO >>", 3)

