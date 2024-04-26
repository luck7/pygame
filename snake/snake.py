import pygame

# Define the game window size
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

directions = ['UP', 'DOWN', 'LEFT', 'RIGHT'] 

# Define the snake's initial position and direction
SNAKE_X = 100
SNAKE_Y = 100
SNAKE_DIRECTION = "RIGHT"

# Define the food's initial position
FOOD_X = 300
FOOD_Y = 300

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the snake sprite
snake = pygame.sprite.Sprite()
snake.image = pygame.Surface((10, 10))
snake.image.fill((0, 255, 0))
snake.rect = snake.image.get_rect()
snake.rect.x = SNAKE_X
snake.rect.y = SNAKE_Y

# Create the food sprite
food = pygame.sprite.Sprite()
food.image = pygame.Surface((10, 10))
food.image.fill((255, 0, 0))
food.rect = food.image.get_rect()
food.rect.x = FOOD_X
food.rect.y = FOOD_Y

# Game loop
while True:

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                SNAKE_DIRECTION = "UP"
            elif event.key == pygame.K_DOWN:
                SNAKE_DIRECTION = "DOWN"
            elif event.key == pygame.K_LEFT:
                SNAKE_DIRECTION = "LEFT"
            elif event.key == pygame.K_RIGHT:
                SNAKE_DIRECTION = "RIGHT"

    # Move the snake
    snake.rect.x += SNAKE_DIRECTION[0]
    snake.rect.y += SNAKE_DIRECTION[1]

    # Check if the snake has hit the wall or itself
    if snake.rect.x < 0 or snake.rect.x > SCREEN_WIDTH - snake.rect.width:
        # Game over
        print("Game over!")
        pygame.quit()
        sys.exit()

    if snake.rect.y < 0 or snake.rect.y > SCREEN_HEIGHT - snake.rect.height:
        # Game over
        print("Game over!")
        pygame.quit()
        sys.exit()

    # Check if the snake has eaten the food
    if snake.rect.colliderect(food.rect):
        # The snake has eaten the food
        print("You ate the food!")

        # Randomly place the food in a new position
        FOOD_X = random.randint(0, SCREEN_WIDTH - food.rect.width)
        FOOD_Y = random.randint(0, SCREEN_HEIGHT - food.rect.height)
        food.rect.x = FOOD_X
        food.rect.y = FOOD_Y

    # Draw the screen
    screen.fill((0, 0, 0))
    screen.blit(snake.image, snake.rect)
    screen.blit(food.image, food.rect)

    pygame.display.flip()
