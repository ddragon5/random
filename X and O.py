import pygame
import time

background_colour = (20, 189, 172)
has_won = False
pygame.init()
black = (0, 0, 0)
running = True
is_X_turn = True
font = pygame.font.Font('freesansbold.ttf', 64)
sfont = pygame.font.Font('freesansbold.ttf', 32)

grid_size = 420
num_slots = 9
slot_size = grid_size / 3

spots_played = []
X_played = []
O_played = []
centers = []
for j in range(3):
    for i in range(3):
        center_x = (i * slot_size) + (slot_size / 2)
        center_y = (j * slot_size) + (slot_size / 2)
        centers.append((center_x, center_y))

# window setup
screen = pygame.display.set_mode((420, 420))
pygame.display.set_caption('איקס עיגול')
screen.fill(background_colour)
# grid setup 140
pygame.draw.line(screen, black, (140, 0), (140, 420), 4)
pygame.draw.line(screen, black, (280, 0), (280, 420), 4)

pygame.draw.line(screen, black, (0, 140), (420, 140), 4)
pygame.draw.line(screen, black, (0, 280), (420, 280), 4)

pygame.display.flip()


def Get_muose_grid_pos(pos):
    x = pos[0]
    y = pos[1]

    if x < 140 and y < 140:
        grid_pos = 0
    if x < 140 and 140 < y < 280:
        grid_pos = 3
    if x < 140 and y > 280:
        grid_pos = 6
    # 2nt column
    if 280 > x > 140 and y < 280:
        grid_pos = 1
    if 280 > x > 140 and 140 < y < 280:
        grid_pos = 4
    if 280 > x > 140 and y > 280:
        grid_pos = 7
    # 3rd column
    if x > 280 and y < 140:
        grid_pos = 2
    if x > 280 and 140 < y < 280:
        grid_pos = 5
    if x > 280 and y > 280:
        grid_pos = 8
    return grid_pos


def Place(where, turn):
    # tarnsle grid pos to centers
    center = centers[where]

    if turn:
        X = font.render('X', True, (84, 84, 84))
        RectX = X.get_rect()
        RectX.center = center
        screen.blit(X, RectX)
    else:
        O = font.render('O', True, (242, 235, 211))
        RectO = O.get_rect()
        RectO.center = center
        screen.blit(O, RectO)


# [(70.0, 70.0), (210.0, 70.0), (350.0, 70.0), (70.0, 210.0), (210.0, 210.0), (350.0, 210.0), (70.0, 350.0), (210.0, 350.0), (350.0, 350.0)]
def check_for_wins(played):
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    if 0 in played and ((1 in played and 2 in played) or (3 in played and 6 in played) or (4 in played and 8 in played)):
        return True
    if 4 in played and ((1 in played and 7 in played) or (3 in played and 5 in played) or (2 in played and 6 in played)):
        return True
    if 8 in played and ((2 in played and 5 in played) or (6 in played and 7 in played)):
        return True

def win_text(won):
    text = font.render(f'{won} HAS WON', True, (232, 14, 14))
    Rect_text = text.get_rect()
    Rect_text.center = (420/2, 420/2)
    screen.blit(text, Rect_text)
    pygame.display.update()
    return True

while running:
    for event in pygame.event.get():
        if not has_won:
            if event.type == pygame.MOUSEBUTTONDOWN:
                muose_grid_pos = Get_muose_grid_pos(pygame.mouse.get_pos())
                print(muose_grid_pos)
                if not muose_grid_pos in spots_played:
                    Place(muose_grid_pos, is_X_turn)
                    spots_played.append(muose_grid_pos)
                    if is_X_turn:
                        X_played.append(muose_grid_pos)
                        X_played.sort()
                        if check_for_wins(X_played):
                            has_won = win_text('X')
                    else:
                        O_played.append(muose_grid_pos)
                        O_played.sort()
                        if check_for_wins(O_played):
                            has_won = win_text('O')
                    is_X_turn = not is_X_turn
            if event.type == pygame.QUIT:
                running = False
            pygame.display.update()
        if has_won:
            if event.type == pygame.QUIT:
                running = False










