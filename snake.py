import pygame
import time
import random

pygame.init()

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (139, 69, 19)

# Display dimensions
width = 600
height = 400
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

# Snake block size
block_size = 15
snake_speed = 10  # Slower snake speed

font_style = pygame.font.SysFont("bahnschrift", 30)
score_font = pygame.font.SysFont("comicsansms", 35)

# Function to display the score
def your_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    game_display.blit(value, [0, 0])

# Function to draw the snake
def our_snake(block_size, snake_list):
    for x in snake_list:
        pygame.draw.rect(game_display, green, [x[0], x[1], block_size, block_size])

# Function to display the message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [width / 6, height / 3])

# Function to create obstacles
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(game_display, brown, [obstacle[0], obstacle[1], block_size, block_size])

# Main function
def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, width - block_size) / 15.0) * 15.0
    foody = round(random.randrange(0, height - block_size) / 15.0) * 15.0

    obstacles = [
        [random.randrange(0, width - block_size, block_size), random.randrange(0, height - block_size, block_size)]
        for _ in range(5)
    ]
    
    while not game_over:

        while game_close:
            game_display.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        game_display.fill(blue)

        # Draw food
        pygame.draw.rect(game_display, yellow, [foodx, foody, block_size, block_size])

        # Draw obstacles
        draw_obstacles(obstacles)

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Check if snake collides with obstacles
        for obstacle in obstacles:
            if x1 == obstacle[0] and y1 == obstacle[1]:
                game_close = True

        our_snake(block_size, snake_List)
        your_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - block_size) / 15.0) * 15.0
            foody = round(random.randrange(0, height - block_size) / 15.0) * 15.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
