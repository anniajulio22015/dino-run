import pygame
import random
import sys
import os

pygame.init()
WIDTH, HEIGHT = 900, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run Adventure")
clock = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", 24)

# Colors
BG_COLOR = (135, 206, 235)
BROWN = (120, 80, 40)
RED = (220, 60, 60)
WHITE = (255, 255, 255)

# Load sprites
flor_normal_img= pygame.image.load(os.path.join("images","flor normal.png")).convert_alpha()
agachada_img= pygame.image.load(os.path.join("images","agachada.png")).convert_alpha()
fuego_img= pygame.image.load(os.path.join("images","fuego.png")).convert_alpha()
roca_img= pygame.image.load(os.path.join("images","roca.png")).convert_alpha()
pajaro_img= pygame.image.load(os.path.join("images","pajaro azul.png")).convert_alpha()

# Scale sprites to expected sizes
flor_normal_IMG = pygame.transform.scale(flor_normal_img, (60, 80))
agachada_IMG = pygame.transform.scale(agachada_img, (60, 40))
fuego_IMG = pygame.transform.scale(fuego_img, (30, 60))
roca_IMG = pygame.transform.scale(roca_img, (40, 40))
pajaro_IMG = pygame.transform.scale(pajaro_img, (50, 30))


def run_game():
    # Dino settings
    dino_img = flor_normal_IMG
    dino = pygame.Rect(80, HEIGHT - 120, 60, 80)
    dino_vel_y = 0
    gravity = 0.8
    jump_strength = -15
    on_ground = True
    is_ducking = False

    # Ground
    ground_y = HEIGHT - 40

    # Obstacles and birds
    obstacles = []   # list of (rect, image)
    pajaros = []       # list of rects
    spawn_timer = 0
    spawn_delay = 90

    # Score
    score = 0
    speed = 6

    running = True
    while running:
        clock.tick(60)
        screen.fill(BG_COLOR)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed() 

        # Jump
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and on_ground:
            dino_vel_y = jump_strength
            on_ground = False

        # Duck
        if keys[pygame.K_DOWN] and on_ground:
            if not is_ducking:
                dino_img = agachada_img
                dino.height = 40
                dino.y += 40
                is_ducking = True
        else:
            if is_ducking:
                dino_img = flor_normal_IMG
                dino.y -= 40
                dino.height = 80
                is_ducking = False

        # Dino physics
        dino_vel_y += gravity
        dino.y += dino_vel_y

        if dino.bottom >= ground_y:
            dino.bottom = ground_y
            dino_vel_y = 0
            on_ground = True

        # Spawn obstacles and birds
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            choice = random.choice(["fuego", "roca", "pajaro"])

            if choice == "fuego":
                rect = pygame.Rect(WIDTH + 20, ground_y - 60, 30, 60)
                obstacles.append((rect, fuego_IMG))

            elif choice == "roca":
                rect = pygame.Rect(WIDTH + 20, ground_y - 40, 40, 40)
                obstacles.append((rect, roca_IMG))

            else:
                # Pájaros a altura que obliga a agacharse
                y = random.choice([ground_y - 80, ground_y - 90])
                pajaro= pygame.Rect(WIDTH + 20, y, 50, 30)
                pajaros.append(pajaro)

            spawn_timer = 0
            if spawn_delay > 50:
                spawn_delay -= 1

        # Move obstacles
        for rect, img in obstacles[:]:
            rect.x -= speed
            if rect.right < 0:
                obstacles.remove((rect, img))
                score += 1

        # Move birds
        for pajaro in pajaros[:]:
            pajaro.x -= speed + 2
            if pajaro.right < 0:
                pajaros.remove(pajaro)
                score += 2

        # Collision
        for rect, img in obstacles:
            if dino.colliderect(rect):
                running = False

        for pajaro in pajaros:
            if dino.colliderect(pajaro):
                running = False

        # Increase speed
        speed = 6 + score // 20

        # Draw ground
        pygame.draw.rect(screen, BROWN, (0, ground_y, WIDTH, 40))

        # Draw dino sprite
        screen.blit(dino_img, (dino.x, dino.y))

        # Draw obstacles
        for rect, img in obstacles:
            screen.blit(img, (rect.x, rect.y))

        # Draw birds
        for pajaro in pajaros:
            screen.blit(pajaro_IMG, (pajaro.x, pajaro.y))

        # UI
        score_text = FONT.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()

    # Game Over screen
    while True:
        screen.fill(BG_COLOR)
        over_text = FONT.render("GAME OVER", True, RED)
        score_text = FONT.render(f"Final Score: {score}", True, WHITE)
        restart_text = FONT.render("Press R to Restart", True, WHITE)

        screen.blit(over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 40))
        screen.blit(score_text, (WIDTH // 2 - 110, HEIGHT // 2))
        screen.blit(restart_text, (WIDTH // 2 - 130, HEIGHT // 2 + 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    return


# Main loop
while True:
    run_game()