import pygame
import random

# Initialize pygame
pygame.init()

# Set up the game window
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)

# Define snake initial position and size
snake_size = 20
x = width // 2
y = height // 2

# Define snake movement variables
x_change = 0
y_change = 0

# Create clock object to control the frame rate
clock = pygame.time.Clock()

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # Change snake direction with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_size

    # Update snake position
    x += x_change
    y += y_change

    # Clear the screen
    screen.fill(black)

    # Draw the snake
    pygame.draw.rect(screen, green, (x, y, snake_size, snake_size))

    # Update the display
    pygame.display.update()

    # Limit frames per second
    clock.tick(10)

# Quit the game
pygame.quit()