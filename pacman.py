import math
import pygame
from board import boards

pygame.init()

WIDTH = 900
HEIGHT = 950
PI = math.pi
screen = pygame.display.set_mode([WIDTH, HEIGHT])
timer = pygame.time.Clock()
fps = 60
font = pygame.font.Font('freesansbold.ttf', 20)
level = boards[0]
background_color = 'black'
ghost_door_color = 'white'
primary_color = 'white'
secondary_color = 'blue'


def draw_board(level):
    tile_height = ((HEIGHT - 50) // 32)
    tile_width = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(
                    screen, primary_color, (j * tile_width + (0.5 * tile_width), i * tile_height + (0.5 * tile_height)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(
                    screen, primary_color, (j * tile_width + (0.5 * tile_width), i * tile_height + (0.5 * tile_height)), 10)
            if level[i][j] == 3:
                pygame.draw.line(
                    screen, secondary_color,
                    (j * tile_width + (0.5 * tile_width), i * tile_height),
                    (j * tile_width + (0.5 * tile_width), i * tile_height + tile_height), 3)
            if (level[i][j] == 4) | (level[i][j] == 9):
                pygame.draw.line(
                    screen, secondary_color if level[i][j] == 4 else ghost_door_color,
                    (j * tile_width, i * tile_height + (0.5 * tile_height)),
                    (j * tile_width + tile_width, i * tile_height + (0.5 * tile_height)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(
                    screen, secondary_color,
                    [(j * tile_width - (tile_width * 0.4)) - 2, (i * tile_height + (0.5 * tile_height)), tile_width, tile_height], 0, PI/2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(
                    screen, secondary_color,
                    [(j * tile_width + (tile_width * 0.5)), (i * tile_height + (0.5 * tile_height)), tile_width, tile_height], PI/2, PI, 3)
            if level[i][j] == 7:
                pygame.draw.arc(
                    screen, secondary_color,
                    [(j * tile_width + (tile_width * 0.5)), (i * tile_height - (0.4 * tile_height)), tile_width, tile_height], PI, 3*PI/2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(
                    screen, secondary_color,
                    [(j * tile_width - (tile_width * 0.4)) - 2, (i * tile_height - (0.4 * tile_height)), tile_width, tile_height], 3*PI/2, 2*PI, 3)


run = True
while run:
    timer.tick(fps)
    screen.fill(background_color)
    draw_board(level)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()
