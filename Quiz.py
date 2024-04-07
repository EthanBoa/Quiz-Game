from time import sleep
import random

questoes =[
    "Quem é o cineasta moçambicano conhecido por seu filme O Jardim das Folhas Sagradas?",
    "Qual é o nome do grupo musical moçambicano que popularizou o estilo musical Marrabenta?",
    "Quem é o artista plástico moçambicano que ganhou reconhecimento internacional por suas obras?"
]

pontuacao = 0

print("="*30, "BEM VINDO AO QUIZ", "="*30)

while True:
    q = random.choice(questoes) #selecionando a questao
    print("\033[33m....................................Pensando numa pergunta.........................\033[m")
    sleep(3)
    
    

    print (q) #pergunta lancada
    sleep(1.5)
    
    print("=="*50)
    resposta_do_Usuario = str(input("Sua resposta: ")).lower() #O usuaria devera colocar a sua resposta

#Analise das respostas
    if questoes == questoes[0]:
        resposta_do_Usuario = "gilberto mendes"
        print("Vc ganhou +10 potos")
    else:
        print("vc perdeu")
    
    break
    
    