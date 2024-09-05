frase = input('\033[36mDigite uma frase\033[0m: ')

quantidade = frase.lower().count('a')

if quantidade > 0:
    print(f"\033[36mA letra 'a' aparece \033[37m{quantidade}\033[36m vez(es)\033[0m")
else:
    print("\033[31mA letra 'a' não apareceu nenhuma vez na frase.\033[0m")
