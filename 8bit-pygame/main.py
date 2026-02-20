# 8-Bit Vertical Runner Game using Pygame

import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 720, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("8-Bit Vertical Runner")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BACKGROUND = (65, 25, 64)
BUTTON_LIGHT = (169, 169, 169)
BUTTON_DARK = (100, 100, 100)

# Player settings
player_size = 40
player_x = 40
player_y = HEIGHT // 2
player_color = random.choice([RED, BLUE, (0, 255, 0)])

# Enemy settings
enemy_size = 50
enemy_x = WIDTH
enemy_y = random.randint(50, HEIGHT - 50)

# Score block settings
score_x = WIDTH + 100
score_y = random.randint(50, HEIGHT - 50)

# Game variables
speed = 10
score = 0
font = pygame.font.SysFont("Corbel", 35)


def game_over():
    """Game Over screen"""
    while True:
        screen.fill(BACKGROUND)
        over_text = font.render("GAME OVER", True, WHITE)
        restart_text = font.render("Restart", True, WHITE)
        exit_text = font.render("Exit", True, WHITE)

        mouse = pygame.mouse.get_pos()

        # Restart Button
        pygame.draw.rect(screen, BUTTON_DARK, [250, 350, 200, 50])
        screen.blit(restart_text, (300, 360))

        # Exit Button
        pygame.draw.rect(screen, BUTTON_DARK, [250, 420, 200, 50])
        screen.blit(exit_text, (330, 430))

        screen.blit(over_text, (260, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < mouse[0] < 450 and 350 < mouse[1] < 400:
                    main_game()
                if 250 < mouse[0] < 450 and 420 < mouse[1] < 470:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


def main_game():
    """Main game loop"""
    global player_y, enemy_x, enemy_y, score_x, score_y, score, speed

    player_y = HEIGHT // 2
    enemy_x = WIDTH
    enemy_y = random.randint(50, HEIGHT - 50)
    score_x = WIDTH + 100
    score_y = random.randint(50, HEIGHT - 50)
    score = 0
    speed = 10

    while True:
        screen.fill(BACKGROUND)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            player_y -= 10
        if keys[pygame.K_DOWN]:
            player_y += 10

        # Keep player inside screen
        if player_y <= 40 or player_y >= HEIGHT - 40:
            game_over()

        # Enemy movement
        enemy_x -= speed
        if enemy_x < 0:
            enemy_x = WIDTH
            enemy_y = random.randint(50, HEIGHT - 50)

        # Score block movement
        score_x -= speed
        if score_x < 0:
            game_over()

        # Collision detection (enemy)
        if (
            player_x < enemy_x + enemy_size
            and player_x + player_size > enemy_x
            and player_y < enemy_y + enemy_size
            and player_y + player_size > enemy_y
        ):
            game_over()

        # Collision detection (score block)
        if (
            player_x < score_x + enemy_size
            and player_x + player_size > score_x
            and player_y < score_y + enemy_size
            and player_y + player_size > score_y
        ):
            score += 1
            speed += 1
            score_x = WIDTH + 100
            score_y = random.randint(50, HEIGHT - 50)

        # Draw objects
        pygame.draw.rect(screen, player_color, [player_x, player_y, player_size, player_size])
        pygame.draw.rect(screen, RED, [enemy_x, enemy_y, enemy_size, enemy_size])
        pygame.draw.rect(screen, BLUE, [score_x, score_y, enemy_size, enemy_size])

        # Display score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (WIDTH - 180, HEIGHT - 40))

        pygame.display.update()
        clock.tick(60)


def intro_screen():
    """Intro menu"""
    while True:
        screen.fill(BACKGROUND)
        title = font.render("8-Bit Vertical Runner", True, WHITE)
        start_text = font.render("Start Game", True, WHITE)
        exit_text = font.render("Exit", True, WHITE)

        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(screen, BUTTON_DARK, [250, 350, 220, 50])
        pygame.draw.rect(screen, BUTTON_DARK, [250, 420, 220, 50])

        screen.blit(title, (180, 200))
        screen.blit(start_text, (280, 360))
        screen.blit(exit_text, (330, 430))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 250 < mouse[0] < 470 and 350 < mouse[1] < 400:
                    main_game()
                if 250 < mouse[0] < 470 and 420 < mouse[1] < 470:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        clock.tick(60)


# Start the game
intro_screen()