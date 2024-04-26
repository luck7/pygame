import pygame

# Initialize Pygame
pygame.init()

# Set up the display
win = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rectangle Example")

# Draw a rectangle
pygame.draw.rect(win, (255, 0, 0), (100, 100, 200, 150))

# Update the display
pygame.display.flip()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit the game
pygame.quit()