import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((250, 250))
# Example game map
game_map = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 2, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
]

# Meaning of numbers:
# 1 = Wall, 0 = Floor, 2 = Player spawn

# Define colors
colors = {
    0: (200, 200, 200),  # Floor (Gray)
    1: (100, 100, 100),  # Wall (Dark Gray)
    2: (0, 255, 0)       # Player Spawn (Green)
}

tile_size = 50  # Size of each tile

def draw_map():
    for row_index, row in enumerate(game_map):
        for col_index, tile in enumerate(row):
            pygame.draw.rect(
                screen,
                colors[tile],
                (col_index * tile_size, row_index * tile_size, tile_size, tile_size)
            )

# Game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen
    draw_map()  # Draw game map
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Refresh display

pygame.quit()
