from time import sleep
def exibir_carregamento(frase, segundos=5):
    print(frase, end='', flush=True)
    for _ in range(segundos):
        print(".", end='', flush=True)
        sleep(1)
    print('')
def pertence_fibonacci(numero):
    if numero < 0:
        return False
    a, b = 0, 1

    while a < numero:
        a, b = b, a + b

    return a == numero

try:
    numero = int(input('Digite um\033[34m\033[1m número\033[0m para verificar se pertence à sequência de\033[34m\033[1m FIBONACCI\033[0m: '))
    if pertence_fibonacci(numero):
        exibir_carregamento('Processando', 3)
        print(f'\033[32m\033[1mO número \033[34m\033[1m{numero}\033[32m\033[1m pertence à sequência\033[0m')
    else:
        exibir_carregamento('Processando', 3)
        print(f'\033[31m\033[1mO número \033[34m\033[1m{numero}\033[31m\033[1m não pertence.\033[0m')
except ValueError:
    print('\033[31m\033[1mErro: Digite um número inteiro válido.\033[0m')
