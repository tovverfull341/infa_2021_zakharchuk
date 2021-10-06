import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((1000, 600))
FPS = 30

yellow=(246,153,0)
red=(222,138,138)
pink=(246,143,150)
orange=(246,112,0)
p_1=(255,204,229)
purple=(200,153,255)
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


    points_1=((0,360),(27,293),(209,65),(277,115),(291,163)
    ,(403,269),(517,259),(561,291),(609,257),(657,275),(715,273),(781,189)
            ,(831,149),(873,181),(889,233),(1000,250),(0,360))
    points_2=((0,420),(0,350),(60,227),(117,215),(153,235),(183,339),(219,275),(269,299),(313,257)
    ,(359,271),(397,335),(483,307),(531,247),(573,227),(605,229),(629,269),(661,303),(743,271)
          ,(805,331),(845,277),(917,287),(1000,227),(1000,420),(0,420))
    strip(pink,0,0,1000,600)
    strip(p_1,0,120,1000,120)
    strip(purple,0,360,1000,240)
    mount_1(orange)
    mount_2(red)
    sun(yellow, 50, 450, 100)

main()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

