# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

# Defina os códigos de escape ANSI para as cores


# Defina os códigos de escape ANSI para as cores
cor_vermelha = "\033[91m"
cor_verde = "\033[92m"
cor_amarela = "\033[93m"
reset_cor = "\033[0m"
fundo_branco = '\033[47m'

# Código de escape ANSI para fonte maior
fonte_maior = "\033[50m"
reset_fonte = "\033[0m"


# Use os códigos de escape ANSI para definir a cor da fonte na saída do print
# print(cor_vermelha + "Isso é vermelho!" + reset_cor)
# print(cor_verde + "Isso é verde!" + reset_cor)
# print(cor_amarela + "Isso é amarelo!" + reset_cor)

print("\n******************* Calculadora em Python *******************")

def adicao(x, y):
    return x + y
    
def subtracao(x, y):
    return x - y

def multiplicao(x, y):
    return x * y

def divisao(x, y):
    return x / y

print("\n Selecione um numero da operação desejada: " )
print("\n1 - Adição ( + )")
print("2 - Subtração ( - )")
print("3 - Multiplicação ( * )" )
print("4 - Divisão ( / )")
print("\n")


while True:
    try:
        operador = int(input("Selecione um numero da operação desejada: "))
        print("\n")

        numero1 = float(input("Digite o primeiro número do cálculo "))
        numero2 = float(input("Digite o segundo número do cálculo "))

        
        if operador < 1 or operador > 4:
            print("Escolha um número entre 1 e 4")
        elif operador == 4 and numero2 <= 0:
            print("Se o operador for de divisão, o segundo número não pode ser menor ou igual a 0.")
        else:
            break

    except ValueError:
        print("Entrada inválida. Certifique-se de que o operador seja um número inteiro.") 


if operador == 1:
    print("\n")
    print(numero1, "+", numero2, "=", adicao(numero1, numero2))
    print("\n")

elif operador == 2:
    print("\n")
    print(numero1, "-", numero2, "=", subtracao(numero1, numero2))
    print("\n")

elif operador == 3:
    print("\n")
    print(numero1, "*", numero2, "=", multiplicao(numero1, numero2))
    print("\n")

elif operador == 4:
    print("\n")
    print(numero1, "/", numero2, "=", divisao(numero1, numero2))
    print("\n")

else:
    print("Escolha uma operação válida")