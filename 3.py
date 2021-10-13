import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
FPS = 30

black=(0,0,0)
yellow=(246,153,0)
red=(222,138,138)
pink=(246,143,150)
orange=(246,112,0)
p_1=(255,204,229)
purple=(200,153,255)
p_2=(62,50,105)

'''Главная функция'''
def main():
    """Солнце"""
    def sun(color, rad, cx, cy):
        circle(screen, color, (cx, cy), rad)
        """Разноцветные полоски, создающие фон"""
    def strip(color, beg_x, beg_y, length, width):
        rect(screen, color, (beg_x, beg_y, length, width))
        """Первый горный массив"""
    def mount_1(color):
        polygon(screen,color,points_1)
        """Второй горный массив"""
    def mount_2(color):
        polygon(screen,color,points_2)
        """Третий горный массив"""
    def mount_3(color):
        polygon(screen,color,points_3)
    strip(pink, 0, 0, 1000, 600)
    strip(p_1, 0, 120, 1000, 120)
    strip(purple, 0, 360, 1000, 240)
    mount_1(orange)
    mount_2(red)
    mount_3(p_2)
    sun(yellow, 50, 450, 100)
    """Живность"""
def bird(mx,my,color,scale):
    points_b = ((mx, my), (mx + 8 / scale, my + 26/scale), (mx + 80/scale,my + 59/scale),
                (mx + 153 / scale, my + 6 / scale),
                (mx + 158 / scale, my - 19 / scale), (mx + 134/ scale, my - 10 / scale),
                (mx + 77 / scale, my + 25 / scale),
                (mx + 31 / scale, my - 1 / scale), (mx, my))
    polygon(screen,color,points_b)


points_1=((0,360),(27,293),(209,65),(277,115),(291,163)
    ,(403,269),(517,259),(561,291),(609,257),(657,275),(715,273),(781,189)
            ,(831,149),(873,181),(889,233),(1000,250),(0,360))
points_2=((0,420),(0,350),(60,227),(117,215),(153,235),(183,339),(219,275),(269,299),(313,257)
    ,(359,271),(397,335),(483,307),(531,247),(573,227),(605,229),(629,269),(661,303),(743,271)
          ,(805,331),(845,277),(917,287),(1000,227),(1000,420),(0,420))
points_3=((0,305),(85,329),(191,505),(263,548),(328,572),(502,475),(606,522),(695,538),
              (764,490),(796,425),(846,360),(900,350),(1000,331),(1000,600),(0,600),(0,305))


main()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

for i in range(300):
    main()
    bird(i+50,i,black,1)
    bird(1000-i,400-i,black,2)
    bird(500,i,black,3)
    bird(i,500,black,1)
    bird(i,200,black,1.5)
    pygame.display.update()
    clock.tick(100)
for i in range(100):
    main()
    bird(350-i,300-i,black,1)
    bird(700+i,100+i,black,2)
    bird(500,300-i,black,3)
    bird(300-i,500,black,1)
    bird(300-i,200,black,1.5)
    pygame.display.update()
    clock.tick(100)

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
