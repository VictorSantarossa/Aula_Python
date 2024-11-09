import pygame
import random
import sys

# Inicializando o Pygame
pygame.init()

# Definindo as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)

# Tamanho da tela (resolução aumentada)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo da Forca")

# Lista de palavras e dicas
palavras_com_dicas = [
    {"palavra": "PYTHON", "dica": "Uma linguagem de programação popular."},
    {"palavra": "DESENVOLVEDOR", "dica": "Profissional que cria software."},
    {"palavra": "JOGO", "dica": "Entretenimento digital."},
    {"palavra": "COMPUTADOR", "dica": "Máquina usada para processar dados."},
    {"palavra": "INTELIGENCIA", "dica": "Capacidade de aprender e resolver problemas."},
    {"palavra": "PROGRAMACAO", "dica": "Ato de escrever código."},
    {"palavra": "ALGORITMO", "dica": "Conjunto de passos para resolver um problema."},
    {"palavra": "DESIGN", "dica": "Processo criativo para desenvolver produtos."},
    {"palavra": "APRENDIZADO", "dica": "Aquisição de conhecimento."},
    {"palavra": "CÓDIGO", "dica": "Conjunto de instruções de programação."},
]

# Sorteia uma palavra e sua dica
escolha = random.choice(palavras_com_dicas)
palavra_secreta = escolha["palavra"]
dica = escolha["dica"]
letras_acertadas = ['_'] * len(palavra_secreta)
letras_erradas = []
tentativas = 6
pontuacao = 100  # Começa com mais pontos
dicas_usadas = 0
max_dicas = 3  # Limite de dicas que o jogador pode usar

# Definindo fontes
font = pygame.font.Font(None, 40)
title_font = pygame.font.Font(None, 60)
dica_font = pygame.font.Font(None, 30)

# Função para exibir o texto na tela
def exibir_texto(texto, cor, y_offset=0, font_size=36):
    font = pygame.font.Font(None, font_size)
    text = font.render(texto, True, cor)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 + y_offset))

# Função para desenhar o fundo
def desenhar_fundo():
    screen.fill(GRAY)

# Função para desenhar o desenho do enforcado (mais à esquerda)
def desenhar_enforcado(tentativas_erradas):
    # Posição inicial do enforcado
    x_pos = 100
    y_pos = 200

    # Cabeça
    if tentativas_erradas >= 1:
        pygame.draw.circle(screen, BLACK, (x_pos + 30, y_pos), 30, 5)  # Cabeça
    # Corpo
    if tentativas_erradas >= 2:
        pygame.draw.line(screen, BLACK, (x_pos + 30, y_pos + 30), (x_pos + 30, y_pos + 100), 5)  # Corpo
    # Braços
    if tentativas_erradas >= 3:
        pygame.draw.line(screen, BLACK, (x_pos + 30, y_pos + 50), (x_pos, y_pos + 70), 5)  # Braço esquerdo
    if tentativas_erradas >= 4:
        pygame.draw.line(screen, BLACK, (x_pos + 30, y_pos + 50), (x_pos + 60, y_pos + 70), 5)  # Braço direito
    # Pernas
    if tentativas_erradas >= 5:
        pygame.draw.line(screen, BLACK, (x_pos + 30, y_pos + 100), (x_pos, y_pos + 150), 5)  # Perna esquerda
    if tentativas_erradas >= 6:
        pygame.draw.line(screen, BLACK, (x_pos + 30, y_pos + 100), (x_pos + 60, y_pos + 150), 5)  # Perna direita

# Função para desenhar a palavra
def desenhar_palavra():
    palavra_exibida = " ".join(letras_acertadas)
    exibir_texto(palavra_exibida, BLACK, -100)

# Função para desenhar dicas
def desenhar_dica():
    exibir_texto(f"Dica: {dica}", BLUE, 180, font_size=30)

# Função para a tela de introdução
def tela_inicial():
    desenhar_fundo()
    exibir_texto("Jogo da Forca", GREEN, -150, font_size=60)
    exibir_texto("Pressione ENTER para começar", BLUE, 20)
    pygame.display.flip()

    # Aguardar o jogador pressionar ENTER
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    esperando = False

# Função de fim de jogo
def fim_de_jogo(vitoria):
    desenhar_fundo()
    if vitoria:
        exibir_texto("Você venceu!", GREEN, -100, font_size=60)
    else:
        exibir_texto(f"Você perdeu! A palavra era: {palavra_secreta}", RED, -100, font_size=40)

    exibir_texto(f"Pontos: {pontuacao}", BLACK, 50, font_size=40)
    exibir_texto("Pressione ESC para sair ou ENTER para jogar novamente", BLUE, 120)

    pygame.display.flip()

    # Espera pela escolha do jogador
    esperando = True
    while esperando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    reiniciar_jogo()
                    esperando = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

# Função para reiniciar o jogo
def reiniciar_jogo():
    global palavra_secreta, letras_acertadas, letras_erradas, tentativas, pontuacao, dica, dicas_usadas
    escolha = random.choice(palavras_com_dicas)
    palavra_secreta = escolha["palavra"]
    dica = escolha["dica"]
    letras_acertadas = ['_'] * len(palavra_secreta)
    letras_erradas = []
    tentativas = 6
    pontuacao = 100
    dicas_usadas = 0
    jogo()

# Função para dar a dica de uma letra
def dar_dica():
    global pontuacao, dicas_usadas
    if dicas_usadas < max_dicas:
        # Encontre uma letra não revelada na palavra
        letras_na_palavra = [i for i, letra in enumerate(palavra_secreta) if letras_acertadas[i] == '_']
        if letras_na_palavra:
            indice = random.choice(letras_na_palavra)
            letras_acertadas[indice] = palavra_secreta[indice]  # Revela a letra
            pontuacao -= 10  # Perde 10 pontos por cada dica usada
            dicas_usadas += 1
        else:
            exibir_texto("Não há mais dicas disponíveis.", RED, 150)
    else:
        exibir_texto("Você atingiu o limite de dicas.", RED, 150)

# Função principal do jogo
def jogo():
    global tentativas, pontuacao

    rodando = True
    while rodando:
        desenhar_fundo()

        # Desenho do enforcado (mais à esquerda)
        desenhar_enforcado(6 - tentativas)

        # Exibindo palavra
        desenhar_palavra()

        # Exibindo letras erradas
        exibir_texto(f"Letras erradas: {' '.join(letras_erradas)}", RED, 150)

        # Exibindo tentativas restantes
        exibir_texto(f"Tentativas restantes: {tentativas}", BLUE, 200)

        # Exibindo pontuação
        exibir_texto(f"Pontos: {pontuacao}", GREEN, 250)

        # Exibindo dica
        desenhar_dica()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            if event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    letra = chr(event.key).upper()
                    if letra in palavra_secreta:
                        # Atualiza as letras acertadas
                        for i, letra_secreta in enumerate(palavra_secreta):
                            if letra == letra_secreta:
                                letras_acertadas[i] = letra
                        pontuacao += 10  # Aumenta os pontos por acerto
                    else:
                        # Adiciona a letra errada
                        if letra not in letras_erradas:
                            letras_erradas.append(letra)
                            tentativas -= 1
                    if "_" not in letras_acertadas:
                        fim_de_jogo(True)
                        rodando = False

                # Pedir dica
                elif event.key == pygame.K_d:
                    dar_dica()

        # Verifica se o jogador perdeu
        if tentativas == 0:
            fim_de_jogo(False)
            rodando = False

        pygame.display.flip()
        pygame.time.Clock().tick(30)  # Controla a taxa de atualização

# Tela inicial
tela_inicial()

# Inicia o jogo
jogo()

# Finaliza o Pygame
pygame.quit()
