import pygame

pygame.unit()

screen=pygame.display.set_mode((300, 200))



pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
