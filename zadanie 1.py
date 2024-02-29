import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0,0,0)

#funkcja do przechylania powierzchni
def skew_surface(surface, skew_x):
    width, height = surface.get_size()
    new_width = int(width + abs(skew_x) * height)
    
    skewed_surface = pygame.Surface((new_width, height))
    skewed_surface.fill(CZARNY)

    for y in range(height):
        min_x = 0
        max_x = new_width
        for x in range(width):
            if CZERWONY == surface.get_at((int(x), int(y))):
                min_x = x + skew_x * y
                break
        i = width - 1
        while i >= min_x:
            if CZERWONY == surface.get_at((int(i), int(y))):
                max_x = i + skew_x * y
                break
            i -= 1
        if min_x > 0 and max_x < new_width - 1:
            while min_x <= max_x:
                skewed_surface.set_at((int(min_x), y), CZERWONY)
                min_x += 1

    return skewed_surface



# stworzenie listy wierzchołków wielokąta
r = 150
move = 2*math.pi/11
degre = -math.pi/2
list = [[0.5,0.5]]
list.clear()
i = 0
while i < 11:
        list.append([150 + math.cos(degre)*r, 150 + math.sin(degre)*r])
        degre = degre + move
        i = i + 1

activeTransformation = 1

polygon = pygame.Surface((300, 300))
pygame.draw.polygon(polygon, CZERWONY, list)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_1:
                activeTransformation = 1
            if event.key == pygame.K_2:
                activeTransformation = 2
            if event.key == pygame.K_3:
                activeTransformation = 3
            if event.key == pygame.K_4:
                activeTransformation = 4
            if event.key == pygame.K_5:
                activeTransformation = 5
            if event.key == pygame.K_6:
                activeTransformation = 6
            if event.key == pygame.K_7:
                activeTransformation = 7
            if event.key == pygame.K_8:
                activeTransformation = 8
            if event.key == pygame.K_9:
                activeTransformation = 9

    
    win.fill((0,0,0))
    match activeTransformation:
        case 1:
            win.blit(polygon,[150,150])
        case 2:
            oldCenter = win.blit(polygon,[150,150]).center
            rotatedSurf =  pygame.transform.rotate(polygon, -45)
            rotatedSurf = pygame.transform.scale_by(rotatedSurf,(1.8,1.8))
            rotRect = rotatedSurf.get_rect()
            rotRect.center = oldCenter
            win.blit(rotatedSurf, rotRect)
        case 3:
            oldCenter = win.blit(polygon,[150,150]).center
            rotatedSurf =  pygame.transform.flip(polygon, False, True)
            rotatedSurf = pygame.transform.scale(rotatedSurf, [300,500])
            rotRect = rotatedSurf.get_rect()
            rotRect.center = oldCenter
            win.blit(rotatedSurf, rotRect)
        case 4:
            oldCenter = win.blit(polygon,[150,150]).center
            skewPolygon = skew_surface(polygon, 0.3)
            rotRect = skewPolygon.get_rect()
            rotRect.center = oldCenter
            win.blit(skewPolygon, rotRect)
        case 5:
            rescaledSurf = pygame.transform.scale(polygon, [500,220])
            win.blit(rescaledSurf, [50,0])
        case 6:
            oldCenter = win.blit(polygon,[150,150]).center
            skewPolygon = skew_surface(polygon, 0.3)
            rotatedSurf =  pygame.transform.rotate(skewPolygon, -90)
            rotRect = rotatedSurf.get_rect()
            rotRect.center = oldCenter
            win.blit(rotatedSurf, rotRect)
        case 7:
            oldCenter = win.blit(polygon,[150,150]).center
            rotatedSurf =  pygame.transform.rotate(polygon, 180)
            rotatedSurf = pygame.transform.scale(rotatedSurf, [300,500])
            rotRect = rotatedSurf.get_rect()
            rotRect.center = oldCenter
            win.blit(rotatedSurf, rotRect)
        case 8:
            rotatedSurf = pygame.transform.scale(polygon, [450,300])
            rotatedSurf =  pygame.transform.rotate(rotatedSurf, -25)
            win.blit(rotatedSurf, [-30,200])
        case 9:
            rotatedSurf =  pygame.transform.rotate(polygon, 90)
            skewPolygon = skew_surface(rotatedSurf, 0.3)
            rotatedSurf =  pygame.transform.rotate(skewPolygon, 90)
            win.blit(rotatedSurf, [310,150])  

    pygame.display.update()