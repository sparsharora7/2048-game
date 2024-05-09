import pygame
import random

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GRAY = (80, 80, 80)
GREEN = (0, 128, 0)
RED = (128, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
PURPLE = (128, 0, 128)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)

# Constants
WIDTH = 400
HEIGHT = 400
GRID_SIZE = 4
TILE_SIZE = WIDTH // GRID_SIZE

# Color dictionary for different numbers
NUMBER_COLORS = {
    2: WHITE,
    4: YELLOW,
    8: ORANGE,
    16: RED,
    32: PURPLE,
    64: BLUE,
    128: CYAN,
    256: GREEN,
    512: YELLOW,
    1024: ORANGE,
    2048: RED,
    4096: PURPLE,
    8192: BLUE
}

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048 Game")
clock = pygame.time.Clock()

# Function to draw text on the screen
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw the grid
def draw_grid(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            pygame.draw.rect(screen, DARK_GRAY, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
            value = grid[i][j]
            if value != 0:
                tile_color = NUMBER_COLORS.get(value, BLACK)
                font = pygame.font.Font(None, 36)
                pygame.draw.rect(screen, tile_color, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0)
                draw_text(str(value), font, BLACK, j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2)

# Function to add a new tile (2 or 4) to a random empty cell
def add_new_tile(grid):
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if grid[i][j] == 0]
    if empty_cells:
        i, j = random.choice(empty_cells)
        grid[i][j] = random.choice([2, 4])

# Function to move tiles in a specified direction
def move(grid, direction):
    if direction == 'up':
        for j in range(GRID_SIZE):
            for i in range(1, GRID_SIZE):
                if grid[i][j] != 0:
                    for k in range(i, 0, -1):
                        if grid[k-1][j] == 0:
                            grid[k-1][j] = grid[k][j]
                            grid[k][j] = 0
                        elif grid[k-1][j] == grid[k][j]:
                            grid[k-1][j] *= 2
                            grid[k][j] = 0
                            break
                        else:
                            break
    elif direction == 'down':
        for j in range(GRID_SIZE):
            for i in range(GRID_SIZE - 2, -1, -1):
                if grid[i][j] != 0:
                    for k in range(i, GRID_SIZE - 1):
                        if grid[k+1][j] == 0:
                            grid[k+1][j] = grid[k][j]
                            grid[k][j] = 0
                        elif grid[k+1][j] == grid[k][j]:
                            grid[k+1][j] *= 2
                            grid[k][j] = 0
                            break
                        else:
                            break
    elif direction == 'left':
        for i in range(GRID_SIZE):
            for j in range(1, GRID_SIZE):
                if grid[i][j] != 0:
                    for k in range(j, 0, -1):
                        if grid[i][k-1] == 0:
                            grid[i][k-1] = grid[i][k]
                            grid[i][k] = 0
                        elif grid[i][k-1] == grid[i][k]:
                            grid[i][k-1] *= 2
                            grid[i][k] = 0
                            break
                        else:
                            break
    elif direction == 'right':
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE - 2, -1, -1):
                if grid[i][j] != 0:
                    for k in range(j, GRID_SIZE - 1):
                        if grid[i][k+1] == 0:
                            grid[i][k+1] = grid[i][k]
                            grid[i][k] = 0
                        elif grid[i][k+1] == grid[i][k]:
                            grid[i][k+1] *= 2
                            grid[i][k] = 0
                            break
                        else:
                            break

# Function to check if the game is over
def game_over(grid):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 0:
                return False
            if i+1 < GRID_SIZE and grid[i][j] == grid[i+1][j]:
                return False
            if j+1 < GRID_SIZE and grid[i][j] == grid[i][j+1]:
                return False
    return True

# Main game loop
def main():
    grid = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    add_new_tile(grid)
    add_new_tile(grid)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move(grid, 'up')
                    add_new_tile(grid)
                elif event.key == pygame.K_DOWN:
                    move(grid, 'down')
                    add_new_tile(grid)
                elif event.key == pygame.K_LEFT:
                    move(grid, 'left')
                    add_new_tile(grid)
                elif event.key == pygame.K_RIGHT:
                    move(grid, 'right')
                    add_new_tile(grid)

        screen.fill(BLACK)
        draw_grid(grid)
        pygame.display.update()
        clock.tick(30)

        if game_over(grid):
            draw_text("Game Over!", pygame.font.Font(None, 48), WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            break

if __name__ == "__main__":
    main()
