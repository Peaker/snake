#!/usr/bin/env python
import pygame
import random

w = 800
h = 600
pygame.init()
display = pygame.display.set_mode((w,h))

def draw_grid(display):
    color = (255, 0, 0)
    for x in range(0, w+1, w//10):
        pygame.draw.line(display, color, (x, 0), (x, h), 5)
    for y in range(0, h+1, h//10):
        pygame.draw.line(display, color, (0, y), (w, y), 5)

def draw_apple(display, apple_x, apple_y):
    color = (0, 255, 0)
    pygame.draw.ellipse(display, color, ((apple_x*w//10, apple_y*h//10), ((w//10), h//10)))

def draw_snake(display, snake):
    color = (255, 255, 255)
    def pos(x, y): return x*w//10, y*h//10
    for x, y in snake:
        display.fill(color, (pos(x,y), pos(1,1)))

snake = [(0,0), (1,0), (2,0)]

dir_x = 1
dir_y = 0

def randomize_apple(snake):
    while True:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        if (x, y) not in snake:
            return x, y
apple_x, apple_y = randomize_apple(snake)
clock = pygame.time.Clock()
stop = False

def get_dir(key):
    if key == pygame.K_RIGHT:
        return (1, 0)
    if key == pygame.K_LEFT:
        return (-1, 0)
    if key == pygame.K_UP:
        return (0, -1)
    if key == pygame.K_DOWN:
        return (0, 1)

def fps_for(d):
    (dir_x, dir_y) = d
    if dir_y == 1:
        return 1
    if dir_x == -1:
        return 2
    if dir_x == 1:
        return 4
    if dir_y == -1:
        return 3

fps = 1
while not stop:
    display.fill((0,0,0))
    draw_snake(display, snake)
    draw_apple(display, apple_x, apple_y)
    draw_grid(display)
    pygame.display.update()
    clock.tick(fps)
    next_dir_x = dir_x
    next_dir_y = dir_y
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            stop = True
        if ev.type == pygame.KEYDOWN:
            # if ev.key == pygame.K_EQUALS:
            #     fps += 1
            # elif ev.key == pygame.K_MINUS:
            #     fps -= 1
            #     fps = max(fps, 1)
            req = get_dir(ev.key)
            if req is not None:
                req_x, req_y = req
                if dir_x != 0 and req_x != 0:
                    pass
                elif dir_y != 0 and req_y != 0:
                    pass
                else:
                    next_dir_x = req_x
                    next_dir_y = req_y
    dir_x = next_dir_x
    dir_y = next_dir_y
    fps = fps_for((dir_x, dir_y))
    x, y = snake[-1]
    next_x = x + dir_x
    next_y = y + dir_y
    if next_x < 0 or next_x >= 10:
        break
    if next_y < 0 or next_y >= 10:
        break
    if (next_x, next_y) in snake:
        break
    if next_x == apple_x and next_y == apple_y:
        apple_x, apple_y = randomize_apple(snake)
    else:
        snake.pop(0)
    snake.append((next_x, next_y))
