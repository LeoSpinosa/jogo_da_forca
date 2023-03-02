from random import choice
from time import sleep

def regra():
        print("""\nSeja Bem Vindo as regras do Jogo da Forca:
1º regra - Só é possivel informar uma letra por vez.
2º regra - Ao iniciar a partida você tera 7 vidas, cada vida representa uma letra. Apos 7 erros você perde o jogo.
3º regra - Jogo termina ao descobrir a palavra secreta ou caso você perca suas vidas.
Boa sorte...""")

def menuIniciar():
        print("\nCarregando...")
        sleep(2.0)
        print("\nBem vindo ao Jogo da Forca")
        print ("\nEscolha a opção a seguir:") 
        print ("1 - Inicie um jogo")
        print ("2 - Regras")

def divisorias():
        print("="*92)

def pularLinha():
        print("\n") 

forca = """

 _______
        |
        |
        -
"""

vazio = """
        
"""

cabeca = """
        O

"""

tronco = """
        O
        |
"""

bracoEsquerdo = """
        O
       /|
"""

bracoDireito = """
        O
       /|\ 
"""

pernaEsquerda = """
        O
       /|\ 
       /
"""

pernaDireita = """
        O
       /|\ 
       / \ 
"""
palavras = ["VINAGRE","ALFACE","LEOPARDO", "CARANGUEJO", "INSTRUTOR", "PADEIRO", "CARRO", "BICICLETA", "PYTHON", "JAVA"]


while True:
        palavraChave = choice(palavras).upper()
        chances = [vazio,cabeca, tronco, bracoEsquerdo, bracoDireito, pernaEsquerda, pernaDireita]
        letrasAcertadas = ""
        letrasErradas = ""
        count = 0
        erros = 0

        pularLinha()
        divisorias()
        print("""
       _                                 _             ______                               
      | |                               | |           |  ____|                              
      | |   ___     __ _    ___       __| |   __ _    | |__      ___    _ __    ___    __ _ 
  _   | |  / _ \   / _` |  / _ \     / _` |  / _` |   |  __|    / _ \  | '__|  / __|  / _` |
 | |__| | | (_) | | (_| | | (_) |   | (_| | | (_| |   | |      | (_) | | |    | (__  | (_| |
  \____/   \___/   \__, |  \___/     \__,_|  \__,_|   |_|       \___/  |_|     \___|  \__,_|
                    __/ |                                                                   
                   |___/                                                                    
""")

        divisorias()
        menuIniciar()

        opc = int(input("Informe a opção escolhida: "))

        if opc == 1:
                print("\nCarregando...")
                sleep(2.0)
                print("\nTenha um ótimo jogo!")

                while erros != 7:
                        mensagem = ""
                        count = 0

                        for letra in palavraChave:
                                if letra in letrasAcertadas:
                                        mensagem += f"{letra} "
                                        
                                else:
                                        mensagem += "_ "
                                        count += 1

                        pularLinha()
                        divisorias()                
                        print(forca+chances[erros])
                        pularLinha()
                        print(mensagem)
                        pularLinha()

                        if count == 0:
                                print("Parabéns jogador, você descobriu a palavra! \n")
                                sleep(1.5)
                                break
                                  

                        letra = input("Informe uma letra: ").strip().upper()
                        print("\nHmmm... \n")
                        sleep(1.5)

                        if letra in letrasAcertadas+letrasErradas:
                                print("Infelizmente você ja tentou essa letra...")
                                continue

                        elif len(letra) > 1:
                            print("Informação inválida, apenas uma letra por vez!")
                            continue

                        elif letra in palavraChave:
                                print("Opaaa, letra correta!")
                                letrasAcertadas += letra
   
                        else:
                                print("Ops, essa letra não se encontra na palavra!")
                                letrasErradas += letra
                                erros +=1                                 
                        
                if erros == 7:
                        print("\nVishh... Vi que você perdeu suas vidas \nMais sorte na proxima vez.")
                        sleep(1.5) 
                                        
        elif opc == 2:
                print("\nCarregando...")
                sleep(2.0)
                regra()
                sleep(10.0)
                   
        elif 1 != opc != 2:
                print("\nCarregando...")
                sleep(2.0)
                print("\nInformação inválida. \n")                
                continue

        jogarNovamente = str(input("\nDeseja voltar ao menu principal? (Sim ou Não): ")).strip().upper()

        if jogarNovamente[0] == "S":
                print("\nCarregando... \n")
                sleep(2.0)
                continue

        elif jogarNovamente[0] == "N":
                print("\nFoi incrivel jogar com você. \nAte a proxima jogador.")
                print("\nCarregando... \n")
                sleep(2.0)
                break 

        else:

                print("\nValor inválido.")
                print("\nCarregando... \n")
                sleep(2.0) 
                continue                













