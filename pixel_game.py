
import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
FPS = 60
GRID_SIZE = 20

# Colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Initialize screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pixel Game")
clock = pygame.time.Clock()

# Character settings
character_size = 20
character_color = GREEN
character_pos = [WIDTH // 2, HEIGHT // 2]
character_speed = 5

# Draw Grid Function
def draw_grid():
    for x in range(0, WIDTH, GRID_SIZE):
        for y in range(0, HEIGHT, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            if (x // GRID_SIZE) % 2 == 0 and (y // GRID_SIZE) % 2 == 0:
                pygame.draw.rect(screen, RED, rect)
            elif (x // GRID_SIZE) % 2 == 1 and (y // GRID_SIZE) % 2 == 1:
                pygame.draw.rect(screen, BLUE, rect)

# Game Loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_pos[0] -= character_speed
    if keys[pygame.K_RIGHT]:
        character_pos[0] += character_speed
    if keys[pygame.K_UP]:
        character_pos[1] -= character_speed
    if keys[pygame.K_DOWN]:
        character_pos[1] += character_speed

    # Draw everything
    draw_grid()
    pygame.draw.rect(screen, character_color, (*character_pos, character_size, character_size))
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

# Quit the game
pygame.quit()
sys.exit()
