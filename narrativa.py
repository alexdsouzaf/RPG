#FUNCTIONS
import random
import os
from time import sleep


#MENU PRINCIPAL
def menu():
  
  print("-----------------------")
  print("**WELLCOME TO MY CODE**")
  print("-----------------------")
  opcoes_menu()
  escolha = int(input("Digite sua opção: "))

  if escolha == 1:
    os.system('clear')
    play()
    print("Aqui inicia o jogo")
  elif escolha == 2:
    os.system('clear')
    instructions()
    #print("aqui abre uma outra função")
  elif escolha == 3:
    os.system('clear')
    credits()
    #print("Aqui abre uma página de copyright")
    menu()
  else:
    os.system('clear')
    print("Insira um comando válido\n")
    menu()
  

#MENU APARTE
def opcoes_menu():
  print("select something\n(1)play\n(2)instructions\n(3)credits\n")


#RESPECTIVOS CAMINHOS DO MENU
def play():
  print("Allright , here we go....\n\n")
  story_telling()

def instructions():
  print("just choose something when you're asked\n\n")
  menu()

def credits():
  print("just the alex :) thank you for run this project\n\n")
  menu()

def story():
  print("oi , como você está?\n to com preguisa de fazer o resto\n toma o menu denovo\n\n")
  menu()


#GERADOR DE NUMERO RANDOMICO
def dado():
  resultado = random.randint(0,9)
  print(resultado)


#TABELA DE CORES ANSI
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[1;33m"

#BREVE NARRATIVA
#cores ansi usadas
RED   = "\033[1;31m"
YELLOW = "\033[1;33m"
BLUE  = "\033[1;34m"
RESET = "\033[0;0m"

#variavel declarada
resultado = ''

def dado(resultado):
  resultado = random.randint(1,10)
  print(YELLOW + "Seu resultado foi:  " , resultado)
  return resultado
  



def story_telling():
  print("Desconhecido: Aqui começa uma breve aventura...\n")

  print("Desconhecido: Mas antes, vamos definir sua capacidade.. através de sorte\n\n Quer arriscar?\n")
  escolha = int(input("(1)->Não , nem te conheço mermão\n(2)->ta , pode ser\nRESPOSTA:"))

  if escolha == 1:
    print("Desconhecido: CHATAO VOCE\n")
    print("acabou a narração , você não quis participar")
  elif escolha == 2:
    print("Desconhecido: ok , vamos rodar 1d10 e ver no que da\n")
    #dado(resultado)
    if dado(resultado) <= 5:
      print(RED + "Desconhecido: este resultado não foi tão bom...\ntalvez você não sobreviva. Vamos parar por aqui\n A breve aventura foi bem breve mesmo. ")
    else:
        print(BLUE + "Desconhecido: bom, bom ,podemos prosseguir\n")
        combate() 

def combate():
  print(RESET + "Desconhecido: você tem força de vontade\n Será que consegue derrubar uma besta?\nUm lobo selvagem surgiu")
  inimigo()



class inimigo:
  def __init__(self):
    self.nome = 'lobo'
    self.vida = 10
    self.dano = 2
    print("Ele tem: ", self.dano, "pontos de dano")
    print("Ele tem: ", self.vida, "pontos de vida")
    print("é um ", self.nome)


menu()
