import pygame

SIZE = 500, 200
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

rect = pygame.Rect(10, 10, 200, 80)
rect1 = pygame.Rect(80, 10, 200, 80)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(GRAY)
    pygame.draw.rect(screen, GREEN, rect1, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.display.flip()

pygame.quit()