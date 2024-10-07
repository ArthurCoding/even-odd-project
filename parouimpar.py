#PROJETO PAR OU IMPAR
while True:
    try:
        valor = int(input("Digite um valor: "))
        if valor % 2 == 0:
            print('Número par')
        else:
            print('Número ímpar')
    except ValueError:
        print('Digite apenas números')
