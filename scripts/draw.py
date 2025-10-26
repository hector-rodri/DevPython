import pygame, sys

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pintar con el ratón")
screen.fill((255, 255, 255))

draw = False 
radius = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

        if event.type == pygame.MOUSEMOTION:
            if draw:
                x, y = event.pos
                pygame.draw.circle(screen, (0, 0, 0), (x, y), radius)

    pygame.display.flip()
