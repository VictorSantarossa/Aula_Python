import pygame
import random
import math
import time

# Inicializar o pygame
pygame.init()

# Definir cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

# Tamanho da tela (resolução 1920x1080)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Criar a tela
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Jogo Estilo Agar.io")

# FPS
FPS = 60
clock = pygame.time.Clock()

# Jogador
player_radius = 50  # Aumentando o tamanho inicial do jogador
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_speed = 3
player_growth_rate = 0.1  # Taxa inicial de crescimento do jogador
player_health = 100
player_lives = 3  # Jogador começa com 3 vidas
growth_boost_rate = 0.2  # Taxa de crescimento aumentada ao pegar bolinhas
growth_boost_time = 0  # Tempo em que o jogador ficará com crescimento acelerado
max_growth_boost_time = 5  # Tempo máximo de aumento de crescimento (em segundos)

# Objetos (partículas que o jogador pode comer)
food_radius = 10
food_count = 50
foods = []

# Inimigos (células controladas pela IA)
enemy_radius_min = 50
enemy_radius_max = 100
enemies = []

# Função para desenhar o jogador
def draw_player(x, y, radius, color):
    pygame.draw.circle(screen, color, (x, y), radius)

# Função para desenhar o alimento
def draw_food(food):
    pygame.draw.circle(screen, GREEN, (food[0], food[1]), food_radius)

# Função para criar alimentos em posições aleatórias
def create_food():
    x = random.randint(food_radius, SCREEN_WIDTH * 2 - food_radius)
    y = random.randint(food_radius, SCREEN_HEIGHT * 2 - food_radius)
    return [x, y]

# Função para desenhar os inimigos
def draw_enemies():
    for enemy in enemies:
        pygame.draw.circle(screen, enemy['color'], (enemy['x'], enemy['y']), enemy['radius'])

# Função para criar inimigos com tamanhos aleatórios e cores aleatórias
def create_enemy():
    radius = random.randint(enemy_radius_min, enemy_radius_max)
    x = random.randint(radius, SCREEN_WIDTH * 2 - radius)
    y = random.randint(radius, SCREEN_HEIGHT * 2 - radius)
    color = random.choice([RED, YELLOW, PURPLE])  # Escolher uma cor aleatória
    return {'x': x, 'y': y, 'radius': radius, 'color': color}

# Função para verificar colisão entre o jogador e os alimentos
def check_food_collision(player_x, player_y):
    global player_radius, player_growth_rate, growth_boost_time
    eaten_food = []
    for food in foods:
        fx, fy = food
        distance = math.hypot(player_x - fx, player_y - fy)
        if distance < player_radius + food_radius:
            # Jogador comeu a bolinha e o crescimento aumenta
            player_radius += player_growth_rate
            growth_boost_time = max_growth_boost_time  # Inicia o tempo do aumento
            eaten_food.append(food)
    for food in eaten_food:
        foods.remove(food)

# Função para verificar colisão entre o jogador e os inimigos
def check_enemy_collision(player_x, player_y):
    global player_health, player_lives, player_radius
    for enemy in enemies:
        ex, ey, eradius = enemy['x'], enemy['y'], enemy['radius']
        distance = math.hypot(player_x - ex, player_y - ey)
        if distance < player_radius + eradius:
            print(f"COLISÃO: Jogador (raio {player_radius}) colidiu com inimigo (raio {eradius})")
            if player_radius > eradius:
                # O jogador comeu o inimigo (cresce)
                player_radius += player_growth_rate * 10  # Cresce ao comer o inimigo
                enemies.remove(enemy)
                print(f"Jogador cresceu para raio {player_radius}")
            else:
                # O inimigo é maior, jogador perde saúde
                player_health -= 10
                print(f"Jogador perdeu 10 de saúde. Saúde restante: {player_health}")
                if player_health <= 0:
                    player_lives -= 1  # Perde uma vida
                    player_health = 100  # A saúde volta para 100
                    print(f"Jogador perdeu uma vida. Vidas restantes: {player_lives}")
                    if player_lives <= 0:
                        return False  # Game Over
    return True

# Função para movimentar os inimigos em direção ao jogador
def move_enemies_towards_player():
    global player_x, player_y
    for enemy in enemies:
        ex, ey, eradius = enemy['x'], enemy['y'], enemy['radius']
        # Calcula o vetor direção para o jogador
        angle = math.atan2(player_y - ey, player_x - ex)
        enemy_speed = 1
        ex += math.cos(angle) * enemy_speed
        ey += math.sin(angle) * enemy_speed
        enemy['x'] = ex
        enemy['y'] = ey

# Função para aplicar o efeito da câmera (deslocamento)
def apply_camera_offset(offset_x, offset_y):
    global player_x, player_y
    # Aplicar o deslocamento de câmera para que o jogador esteja sempre centralizado
    player_x -= offset_x
    player_y -= offset_y

# Função principal do jogo
def game_loop():
    global player_x, player_y, player_radius, player_health, player_lives, foods, enemies, growth_boost_time, player_growth_rate

    # Criar alimentos e inimigos
    foods = [create_food() for _ in range(food_count)]
    enemies = [create_enemy() for _ in range(5)]

    # Inicializar a posição da câmera
    camera_offset_x, camera_offset_y = 0, 0

    running = True
    last_collision_time = 0  # Variável para controlar a frequência das colisões
    while running:
        screen.fill(BLACK)  # Fundo preto

        # Eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movimentação do jogador (mouse controlado)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - player_y, mouse_x - player_x)
        player_x += math.cos(angle) * player_speed
        player_y += math.sin(angle) * player_speed

        # Verificar colisões com alimentos e atualizar o tamanho do jogador
        check_food_collision(player_x, player_y)

        # Aumentar a taxa de crescimento temporariamente, se necessário
        if growth_boost_time > 0:
            growth_boost_time -= 1 / FPS  # Reduz o tempo de aumento
            player_growth_rate = growth_boost_rate  # Aplicar aumento de crescimento
        else:
            player_growth_rate = 0.1  # Resetar a taxa de crescimento para a normal

        # Verificar colisões com inimigos
        if not check_enemy_collision(player_x, player_y):
            print("Game Over!")  # Para depuração
            running = False

        # Movimentar inimigos em direção ao jogador
        move_enemies_towards_player()

        # Câmera segue o jogador (centro do jogador)
        offset_x = player_x - SCREEN_WIDTH // 2
        offset_y = player_y - SCREEN_HEIGHT // 2

        # Desenhar o jogador (com a cor azul)
        draw_player(player_x - offset_x, player_y - offset_y, player_radius, BLUE)

        # Desenhar os alimentos
        for food in foods:
            draw_food(food)

        # Desenhar os inimigos
        draw_enemies()

        # Desenhar a UI (saúde do jogador e vidas)
        font = pygame.font.Font(None, 36)
        health_text = font.render(f"Health: {player_health}", True, WHITE)
        lives_text = font.render(f"Lives: {player_lives}", True, WHITE)
        size_text = font.render(f"Size: {int(player_radius)}", True, WHITE)
        screen.blit(health_text, (10, 10))
        screen.blit(lives_text, (SCREEN_WIDTH - lives_text.get_width() - 10, 10))
        screen.blit(size_text, (SCREEN_WIDTH // 2 - size_text.get_width() // 2, 10))

        # Atualizar a tela
        pygame.display.flip()

        # Controlar FPS
        clock.tick(FPS)

        # Criar novas bolinhas para garantir que o mapa continue com alimentos
        if len(foods) < food_count:
            foods.append(create_food())

    pygame.quit()

# Iniciar o jogo
game_loop()
