# Projeto  - Desenvolvimento de Game em Linguagem Python

# import
import random
from os import system, name

# Funcao para limpar a tela em cada execucao
def limpa_tela():

    # Windows
    if name == 'nt':
       _ = system('cls')

    # Mac ou Linux
    else:
       _ = system('clear')

#Funcao
def game():
   
   limpa_tela()
   print("\nBem-vindo ao jogo da forca!")
   print("Adivinhe a palavra abaixo:\n")

   # Lista de palavras para o jogo
   palavras = [
    "abacate", "abacaxi", "acerola", "amora", "banana", "caju", "cereja", "damasco",
    "figo", "framboesa", "goiaba", "graviola", "jabuticaba", "jaca", "kiwi", "laranja",
    "limao", "maca", "mamao", "manga", "maracuja", "melancia", "melao", "morango",
    "nectarina", "pera", "pessego", "pitanga", "roma", "tangerina", "uva"]
   
   # Escolha randomicamente uma palavra
   palavra = random.choice(palavras)

   # List Comprehension
   letras_descobertas = ['_' for letra in palavra]

   # Numero de chances
   chances = 6

   # Lista para as letras erradas
   letras_erradas = []

   # Loop enquanto o número de cances for maior do que zero
   while chances > 0:
      
      # Print
      print(" ".join(letras_descobertas))
      print("\nChances restantes:", chances)
      print("Letras erradas:", " ".join(letras_erradas))

      # Tentativa
      tentativa = input("\nDigite uma letra: ").lower()

      # Condicional
      if tentativa in palavra:
         index = 0
        
         for letra in palavra:
            if tentativa == letra:
               letras_descobertas[index] = letra
            index += 1
      else:
         chances -= 1
         letras_erradas.append(tentativa)

      # Condicional
      if "_" not in letras_descobertas:
         print("\nVocê venceu, a palavra era:", palavra)
         break
      
   # Condicional
   if "_" in letras_descobertas:
      print("\nVocê perdeu, a palavra era", palavra)

# Bloco main
if __name__ == "__main__":
   game()
   print("\nParabéns, Você está aprendendo programação em Python com a DSA. :)\n")

