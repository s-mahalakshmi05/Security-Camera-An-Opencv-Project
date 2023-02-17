# install pygame package by using the command "pip install pygame"
import pygame
pygame.init()  # initializing all the imported pygame modules
window = pygame.display.set_mode((1200, 400))
track = pygame.image.load('track6.png')  # loading track into the window
car = pygame.image.load('tesla.png')     # loading car into the window
car = pygame.transform.scale(car, (30, 60))  # resizing the size of tesla
car_x = 155
car_y = 300
focal_dis = 25
cam_x_offset = 0
cam_y_offset = 0
direction = 'up'  # initializing direction as 'up'
drive = True
clock = pygame.time.Clock()  # for maintaining speed of tesla
while drive:
    for event in pygame.event.get():  # getting every event that occurs in pygame
        if event.type == pygame.QUIT:
            drive = False
    clock.tick(60)  # speed value=60
    cam_x = car_x + cam_x_offset + 15
    cam_y = car_y + cam_y_offset + 15

    # getting pixel values(colours in road) for observing purpose
    up_px = window.get_at((cam_x, cam_y - focal_dis))[0]
    down_px = window.get_at((cam_x, cam_y + focal_dis))[0]
    right_px = window.get_at((cam_x + focal_dis, cam_y))[0]
    print(up_px, right_px, down_px)

    # change direction (take turn)
    if direction == 'up' and up_px != 255 and right_px == 255:
        direction = 'right'
        cam_x_offset = 30
        car = pygame.transform.rotate(car, -90)  # turn
    elif direction == 'right' and right_px != 255 and down_px == 255:
        direction = 'down'
        car_x = car_x + 30
        cam_x_offset = 0
        cam_y_offset = 30
        car = pygame.transform.rotate(car, -90)  # turn
    elif direction == 'down' and down_px != 255 and right_px == 255:
        direction = 'right'
        car_y = car_y + 30
        cam_x_offset = 30
        cam_y_offset = 0
        car = pygame.transform.rotate(car, 90)  # turn
    elif direction == 'right' and right_px != 255 and up_px == 255:
        direction = 'up'
        car_x = car_x + 30
        cam_x_offset = 0
        car = pygame.transform.rotate(car, 90)  # turn

    # drive
    if direction == 'up' and up_px == 255:
        car_y = car_y - 2
    elif direction == 'right' and right_px == 255:
        car_x = car_x + 2
    elif direction == 'down' and down_px == 255:
        car_y = car_y + 2

    # blit()=Block Transfer-for copying one surface to another
    window.blit(track, (0, 0))   # placing track
    window.blit(car, (car_x, car_y))  # placing camera and car
    pygame.draw.circle(window, (0, 255, 0), (cam_x, cam_y), 5, 5)  # camera setting
    pygame.display.update()  # updating tesla movements in screen/window



