import pygame
import random

# 游戏窗口大小
WIDTH = 800
HEIGHT = 600

# 蛇身和食物大小
BLOCK_SIZE = 20

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 初始化Pygame
pygame.init()

# 创建游戏窗口
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# 游戏时钟
clock = pygame.time.Clock()

# 蛇的初始位置和速度
snake_x = WIDTH // 2
snake_y = HEIGHT // 2
snake_dx = 0
snake_dy = 0

# 蛇身列表
snake_body = []
snake_length = 1

# 食物位置
food_x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
food_y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE

# 游戏结束标志
game_over = False

# 游戏主循环
while not game_over:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_dx != BLOCK_SIZE:
                snake_dx = -BLOCK_SIZE
                snake_dy = 0
            elif event.key == pygame.K_RIGHT and snake_dx != -BLOCK_SIZE:
                snake_dx = BLOCK_SIZE
                snake_dy = 0
            elif event.key == pygame.K_UP and snake_dy != BLOCK_SIZE:
                snake_dx = 0
                snake_dy = -BLOCK_SIZE
            elif event.key == pygame.K_DOWN and snake_dy != -BLOCK_SIZE:
                snake_dx = 0
                snake_dy = BLOCK_SIZE

    # 更新蛇的位置
    snake_x += snake_dx
    snake_y += snake_dy

    # 判断是否吃到食物
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, WIDTH - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        food_y = random.randint(0, HEIGHT - BLOCK_SIZE) // BLOCK_SIZE * BLOCK_SIZE
        snake_length += 1

    # 更新蛇身列表
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[:-1]

    # 判断是否撞到自己或者撞到边界
    if (snake_x < 0 or snake_x >= WIDTH or
            snake_y < 0 or snake_y >= HEIGHT or
            (snake_x, snake_y) in snake_body[:-1]):
        print("Game Over!")
        game_over = True

    # 绘制游戏窗口
    window.fill(BLACK)
    for body_part in snake_body:
        pygame.draw.rect(window, GREEN, (body_part[0], body_part[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(window, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(10)

# 退出游戏
pygame.quit()