import os
import sys

import pygame
import requests

coords_x = 37.530887
coords_y = 55.703118

z = 17
map_type = 'map'

speed = 0.08

map_file = "map.png"

pygame.init()
screen = pygame.display.set_mode((600, 450))
clock = pygame.time.Clock()
pygame.display.set_caption('Yandex.Maps API')

FPS = 10
running = True

while running:

    move = speed / (z + 1)
    print(z)
    print(move)

    key = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if key[pygame.K_PAGEUP]:
                if z < 17:
                    print('ZOOM +')
                    z += 1
            if key[pygame.K_PAGEDOWN]:
                if z > 0:
                    print('ZOOM -')
                    z -= 1
            if key[pygame.K_s]:
                coords_y -= move
                print('DOWN')
            if key[pygame.K_w]:
                coords_y += move
                print('UP')
            if key[pygame.K_d]:
                coords_x += move
                print('RIGHT')
            if key[pygame.K_a]:
                coords_x -= move
                print('LEFT')
            if key[pygame.K_1]:
                map_type = 'map'
            if key[pygame.K_2]:
                map_type = 'sat'
            if key[pygame.K_3]:
                map_type = 'sat,skl'

    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords_x},{coords_y}&z={z}&l={map_type}"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    with open(map_file, "wb") as file:
        file.write(response.content)

    screen.blit(pygame.image.load(map_file), (0, 0))
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()
os.remove(map_file)
