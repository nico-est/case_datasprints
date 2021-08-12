from collections import Counter


def primeiroNaoRepetido(string):
    # A função Counter retorna um dicionário contendo os caracteres pertencentes à string
    # como chave e a quantidade de vezes em que este aparece na string como valor
    cont = Counter(string)

    # Como o dicionário já se encontra ordenado de acordo com a ordem de aparição dos caracteres,
    # basta verificar, percorrendo a string do início, qual o primeiro caractere a possuir valor 1
    for i in string:
        # if i != ' ': #Caso desejar ignorar a frequência de espaços em branco
        if cont[i] == 1:
            print(i)
            break

string = input('Insira a string a ser analizada: ')

primeiroNaoRepetido(string)
