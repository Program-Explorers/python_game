import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("A Python Game")

x = 50
y = 50

width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if x == 0:
            continue
        x -= vel

    elif keys[pygame.K_RIGHT]:
        if x == 460:
            continue

        x += vel

    elif keys[pygame.K_UP]:
        if y == 0:
            continue

        y -= vel
    elif keys[pygame.K_DOWN]:
        if y == 440:
            continue

        y += vel

    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
