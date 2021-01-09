import pygame
import random
import sys


pygame.init()

blocks = 3
size_block = 160
midth = 15
step = bool(random.randrange(0, 2))
width = size_block * blocks + midth * (blocks + 1)
height = width + size_block + 20
title_rec = pygame.Rect(0, 0, width, size_block + 20)
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
delay_key = 10
score_winner = {'Blue': 0, 'Red': 0}
score = True
win_line = [(0, 0), (0, 0)]
win = False
lines = [[(0, 0), (0, 0), (0, 0)],
         [(0, 0), (0, 0), (0, 0)],
         [(0, 0), (0, 0), (0, 0)]]

screen = pygame.display.set_mode((width, height))
# img = pygame.image.load("ZERO.jpg")
# pygame.display.set_icon(img)
pygame.display.set_caption("КРЕСТики  И  НОЛЬики: X-X-O                ANDREY PROJECT")
clock = pygame.time.Clock()


runGame = True
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
pos = 5


def Restart():
    global matrix
    global win
    global pos
    global step
    global score
    matrix = [[0, 0, 0],
              [0, 0, 0],
              [0, 0, 0]]
    win = False
    pos = 5
    score = True
    step = bool(random.randrange(0, 2))
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, width, height))


def Who_win():
    global win_line
    global score_winner
    global win
    global x
    global y
    global score
    no_zero = True
    Blue_win = False
    Red_win = False
    m = matrix.copy()
    for j in range(blocks):
        for i in range(blocks):
            if m[j][i] == 0:
                no_zero = False
    if m[0][0] == 'x' and m[0][1] == 'x' and m[0][2] == 'x':
        win_line = (lines[0][0], lines[0][2])
        Red_win = True
    elif m[0][0] == 'o' and m[0][1] == 'o' and m[0][2] == 'o':
        win_line = (lines[0][0], lines[0][2])
        Blue_win = True
    elif m[1][0] == 'x' and m[1][1] == 'x' and m[1][2] == 'x':
        win_line = (lines[1][0], lines[1][2])
        Red_win = True
    elif m[1][0] == 'o' and m[1][1] == 'o' and m[1][2] == 'o':
        win_line = (lines[1][0], lines[1][2])
        Blue_win = True
    elif m[2][0] == 'x' and m[2][1] == 'x' and m[2][2] == 'x':
        win_line = (lines[2][0], lines[2][2])
        Red_win = True
    elif m[2][0] == 'o' and m[2][1] == 'o' and m[2][2] == 'o':
        win_line = (lines[2][0], lines[2][2])
        Blue_win = True
    elif m[0][0] == 'x' and m[1][0] == 'x' and m[2][0] == 'x':
        win_line = (lines[0][0], lines[2][0])
        Red_win = True
    elif m[0][0] == 'o' and m[1][0] == 'o' and m[2][0] == 'o':
        win_line = (lines[0][0], lines[2][0])
        Blue_win = True
    elif m[0][1] == 'x' and m[1][1] == 'x' and m[2][1] == 'x':
        win_line = (lines[0][1], lines[2][1])
        Red_win = True
    elif m[0][1] == 'o' and m[1][1] == 'o' and m[2][1] == 'o':
        win_line = (lines[0][1], lines[2][1])
        Blue_win = True
    elif m[0][2] == 'x' and m[1][2] == 'x' and m[2][2] == 'x':
        win_line = (lines[0][2], lines[2][2])
        Red_win = True
    elif m[0][2] == 'o' and m[1][2] == 'o' and m[2][2] == 'o':
        win_line = (lines[0][2], lines[2][2])
        Blue_win = True
    elif m[0][0] == 'x' and m[1][1] == 'x' and m[2][2] == 'x':
        win_line = (lines[0][0], lines[2][2])
        Red_win = True
    elif m[0][0] == 'o' and m[1][1] == 'o' and m[2][2] == 'o':
        win_line = (lines[0][0], lines[2][2])
        Blue_win = True
    elif m[0][2] == 'x' and m[1][1] == 'x' and m[2][0] == 'x':
        win_line = (lines[0][2], lines[2][0])
        Red_win = True
    elif m[0][2] == 'o' and m[1][1] == 'o' and m[2][0] == 'o':
        win_line = (lines[0][2], lines[2][0])
        Blue_win = True
    if Red_win or Blue_win or no_zero:
        win = True
        x = y = 3
        if Red_win and score:
            score_winner['Red'] += 1
            score = False
        elif Blue_win and score:
            score_winner['Blue'] += 1
            score = False


def DrawWindow():
    pygame.draw.rect(screen, (255, 235, 190), title_rec)

    f1 = pygame.font.Font(None, 35)
    f2 = pygame.font.SysFont('serif', 40)
    f3 = pygame.font.SysFont('timesnewroman', 37)
    f4 = pygame.font.SysFont('calibri', 25)

    steep = f3.render("Next step:", True, (10, 10, 10))
    text_red = f1.render(f"Red: {score_winner['Red']}", True, (250, 0, 0))
    text_blue = f1.render(f"Blue: {score_winner['Blue']}", True, (0, 0, 250))
    text = f2.render("Score:", True, (0, 0, 0))
    res = f4.render("Click 'R' to restart", True, (40, 200, 35))

    screen.blit(steep, (240, 110))
    screen.blit(text, (25, 15))
    screen.blit(text_red, (40, 80))
    screen.blit(text_blue, (40, 125))
    if win:
        screen.blit(res, (330, 15))

    if step:
        pygame.draw.rect(screen, (0, 0, 0), (415, 70, 90, 90))
        pygame.draw.rect(screen, (160, 160, 255), (420, 75, 80, 80))
        pygame.draw.circle(screen, BLUE, (420 + 40, 75 + 40), 35, 10)
    else:
        pygame.draw.rect(screen, (0, 0, 0), (415, 70, 90, 90))
        pygame.draw.rect(screen, (255, 160, 160), (420, 75, 80, 80))
        pygame.draw.line(screen, RED, (435, 85), (485, 145), 8)
        pygame.draw.line(screen, RED, (485, 85), (435, 145), 8)

    for row in range(blocks):
        for column in range(blocks):
            cursor = False
            X_ = False
            O_ = False
            color = WHITE

            if row == y and column == x and not win:
                cursor = True
                color = (130, 130, 130)
            if matrix[row][column] == 'x':
                color = (255, 160, 160)
                if cursor and not win:
                    color = (200, 100, 100)
                X_ = True
            elif matrix[row][column] == 'o':
                color = (160, 160, 255)
                if cursor and not win:
                    color = (100, 100, 200)
                O_ = True

            w = column * size_block + (column + 1) * midth
            h = (row + 1) * size_block + (row + 1) * midth + 20
            pygame.draw.rect(screen, color, (w, h, 160, 160))
            lines[row][column] = (w + 80, h + 80)
            if X_:
                pygame.draw.line(screen, RED, (w + 15, h + 10), (w + 145, h + 150), 22)
                pygame.draw.line(screen, RED, (w + 145, h + 10), (w + 15, h + 150), 22)
            elif O_:
                pygame.draw.circle(screen, BLUE, (w + 80, h + 80), 70, 24)
            if win:
                pygame.draw.line(screen, PURPLE, win_line[0], win_line[1], 10)

    pygame.display.update()


while runGame:
    clock.tick(30)
    if delay_key > 0:
        delay_key -= 1

    Who_win()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    keys = pygame.key.get_pressed()
    if win and (keys[pygame.K_r] or keys[pygame.K_BACKSPACE]):
        Restart()
    if keys[pygame.K_UP] and (pos - 3) >= 1 and delay_key == 0 and not win:
        delay_key += 10
        pos -= 3
    elif keys[pygame.K_DOWN] and (pos + 3) <= 9 and delay_key == 0 and not win:
        delay_key += 10
        pos += 3
    elif keys[pygame.K_RIGHT] and delay_key == 0 and (pos - 1) // blocks == pos // blocks and not win:
        delay_key += 10
        pos += 1
    elif keys[pygame.K_LEFT] and delay_key == 0 and (pos - 2) // blocks == (pos - 1) // blocks and not win:
        delay_key += 10
        pos -= 1

    y = (pos - 1) // blocks
    x = (pos - 1) % blocks

    if (keys[pygame.K_x] or keys[pygame.K_KP_ENTER]) and not step and matrix[y][x] == 0 and not win:
        matrix[y][x] = 'x'
        step = True
    elif (keys[pygame.K_o] or keys[pygame.K_KP_ENTER]) and step and matrix[y][x] == 0 and not win:
        matrix[y][x] = 'o'
        step = False

    DrawWindow()


pygame.quit()
