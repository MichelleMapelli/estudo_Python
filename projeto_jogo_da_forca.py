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


