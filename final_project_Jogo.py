import pygame 
import random

# Inicializar o Pygame
pygame.init()

# Definir as dimensões da tela
largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Jogo Pedra, Papel e Tesoura")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

# Fonte
fonte = pygame.font.Font(None, 36)

# Carregar imagens
pedra_img = pygame.image.load('pedra.png')
papel_img = pygame.image.load('papel.png')
tesoura_img = pygame.image.load('tesoura.png')

# Escalonar imagens
pedra_img = pygame.transform.scale(pedra_img, (150, 150))
papel_img = pygame.transform.scale(papel_img, (150, 150))
tesoura_img = pygame.transform.scale(tesoura_img, (150, 150))

def texto(texto, cor, x, y):
    texto_surface = fonte.render(texto, True, cor)
    tela.blit(texto_surface, (x, y))

def jogo():
    # Opções do jogo
    opcoes = ["Pedra", "Papel", "Tesoura"]

    # Loop principal do jogo
    while True:
        tela.fill(branco)
        texto("Escolha sua jogada:", preto, 250, 100)

        # Desenhar botões para as opções do jogo
        for i, opcao in enumerate(opcoes):
            pygame.draw.rect(tela, azul, (250, 150 + i * 150, 150, 150))
            if i == 0:
                tela.blit(pedra_img, (250, 150 + i * 150))
            elif i == 1:
                tela.blit(papel_img, (250, 150 + i * 150))
            elif i == 2:
                tela.blit(tesoura_img, (250, 150 + i * 150))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Verificar se o mouse clicou em algum botão de opção
                for i, opcao in enumerate(opcoes):
                    if 250 <= mouse_x <= 400 and 150 + i * 150 <= mouse_y <= 300 + i * 150:
                        cpu = random.randint(0, 2)
                        resultado = verificar_vencedor(i, cpu)
                        tela.fill(branco)
                        texto(f"Você escolheu: {opcao}", preto, 250, 100)
                        texto(f"O CPU escolheu: {opcoes[cpu]}", preto, 250, 250)
                        texto(resultado, vermelho if resultado == "Você perdeu!" else verde, 250, 400)
                        pygame.display.update()
                        pygame.time.delay(3000)

def verificar_vencedor(jogador, cpu):
    if jogador == cpu:
        return "Empate!"
    elif jogador == 0 and cpu == 2 or jogador == 1 and cpu == 0 or jogador == 2 and cpu == 1:
        return "Você ganhou!"
    else:
        return "Você perdeu!"

jogo()

