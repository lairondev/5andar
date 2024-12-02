import pygame as pg
import sys

# Inicialização do Pygame
pg.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("5º Andar")

# Clock para controlar a taxa de atualização
clock = pg.time.Clock()

# Cores
BLACK = (0, 0, 0)

# Carregar o tile básico
TILE_WIDTH, TILE_HEIGHT = 64, 32
tile_image = pg.image.load("assets/tiles/flora.png").convert_alpha()

# Carregar o sprite do jogador
player_image = pg.image.load("assets/tiles/player.png").convert_alpha()
player_rect = player_image.get_rect()

# Define o mapa como uma matriz
map_data = [
    [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
]

# Função para converter posição de grade para posição isométrica
def grid_to_iso(x, y):
    iso_x = (x - y) * TILE_WIDTH // 2
    iso_y = (x + y) * TILE_HEIGHT // 2
    return iso_x, iso_y
    
# Função para verificar colisão com áreas bloqueadas
def check_collision(x, y):
    # Verifica se a nova posição do jogador está dentro dos limites do mapa e se o tile é bloqueado
    if x < 0 or y < 0 or x >= len(map_data[0]) or y >= len(map_data):
        return True # Fora do mapa
    elif map_data[y][x] == 1:
        return True  # Há colisão
    return False # Sem colisão  
    
# Função para mover o jogador
def move_player(x, y, dx, dy):
    # Nova posição proposta
    new_x = x + dx
    new_y = y + dy
    
    # Verifica se há colisão antes de mover
    if not check_collision(new_x, new_y):
        return new_x, new_y  # Movimento permitido
    return x, y  # Movimento bloqueado    

# Renderizar o mapa
def draw_map():
    for row in range(len(map_data)):
        for col in range(len(map_data[row])):
            if map_data[row][col] == 1:
                iso_x, iso_y = grid_to_iso(col, row)
                screen.blit(tile_image, (iso_x + WIDTH // 2, iso_y + HEIGHT // 4))

# Loop principal do jogo
def main():
    player_x, player_y = 1, 1  # Posição inicial do jogador na grade
    speed = 1  # Velocidade de movimento
    
    while True:
        # Eventos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
                
        # Movimentação do jogador com as teclas de seta
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            player_x, player_y = move_player(player_x, player_y, -1, 0)
        if keys[pg.K_RIGHT]:
            player_x, player_y = move_player(player_x, player_y, 1, 0)
        if keys[pg.K_UP]:
            player_x, player_y = move_player(player_x, player_y, 0, -1)
        if keys[pg.K_DOWN]:
            player_x, player_y = move_player(player_x, player_y, 0, 1)
       
        # Atualiza e desenha na tela
        screen.fill(BLACK)
        draw_map()
        
        # Desenha jogador
        iso_x, iso_y = grid_to_iso(player_x, player_y)
        screen.blit(player_image, (iso_x + WIDTH // 2, iso_y + HEIGHT // 4))
        
        pg.display.flip()
        clock.tick(60)
        
if __name__ == "__main__":
    main()
