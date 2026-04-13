import random
import pygame
import sys
import os
from pygame.locals import *
import board

display_width = 600
display_height = 500
gap = 50
board_width = 7
board_height = 6
tie = 'tie.jpg'
player1 = 'player1win.png'
player2 = 'player2win.png'
red = 'red'
blue = 'blue'
white = Color('white')
bg_color = white


red_img = 'red_button.png'
blue_img = 'blue_button.png'


os.environ['SDL_VIDEO_CENTERED'] = '1'  # open window in center
pygame.init()

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('CONNECT 4!')


def main():
    global red_token, blue_token, board_pic, display, turn_player, game_board
    turn_player = rnd_player()

    board_pic = pygame.image.load('board_pic.png').convert()
    board_pic = pygame.transform.scale(board_pic, (400, 370))
    board_pic_rect = board_pic.get_rect()
    board_pic_rect.x = 100
    board_pic_rect.y = 100

    player1win = pygame.image.load(player1)
    player2win = pygame.image.load(player2)

    red_token = build_btn('red')
    blue_token = build_btn('blue')

    red_token_rect = build_btn_rect('red', red_token)
    blue_token_rect = build_btn_rect('blue', blue_token)

    game_board = board.Board(display)

    game_on = True
    while game_on:  # main game loop
        display.blit(board_pic, board_pic_rect)
        display.blit(red_token, red_token_rect)
        display.blit(blue_token, blue_token_rect)
        game_board.draw_board(display)
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mouse_x, mouse_y = event.pos
                col = clicked_col(mouse_x, mouse_y)
                if col is not None:
                    row = game_board.lowest_spots[col]
                    if row >= 0:
                        ball_animation(row, col)
                        game_board.one_square(row, col).color_token(turn_player, player_img(turn_player))
                        game_board.lowest_spots[col] -= 1
                        game_board.one_square(row, col).draw(display)
                        if check_is_win(row, col, turn_player):
                            if turn_player == 1:
                                player1win = pygame.transform.scale(player1win, (600, 200))
                                pygame.display.update()
                                display.blit(player1win, (-10, -10))
                                pygame.display.flip()
                            else:
                                player2win = pygame.transform.scale(player2win, (600, 100))
                                pygame.display.update()
                                display.blit(player2win, (0, 0))
                                pygame.display.flip()
                            pygame.time.wait(1000)
                            pygame.quit()
                            sys.exit()
                        turn_player *= -1  # change turn
        pygame.display.update()


def player_img(player):
    if player == 1:
        return red_img
    else:
        return blue_img


def build_btn(token_color):
    if token_color == 'red':
        img = red_img
    else:
        img = blue_img
    token = pygame.image.load(img).convert()
    token = pygame.transform.scale(token, (40, 40))
    token.set_colorkey(white)
    return token


def build_btn_rect(colour, token):
    token_rect = token.get_rect()
    if colour == 'red':
        token_rect.x = 30
    else:
        token_rect.x = 520
    token_rect.y = 390
    return token_rect


def clicked_col(x, y):
    for token in game_board.all_squares():
        if token.rect.x <= x <= token.rect.x + 44:
            if token.rect.y <= y <= token.rect.y + 44:
                return token.col
    return None


def ball_animation(row, col):
    empty_img = 'circle-xxl.png'
    for r in range(row):
        game_board.one_square(r, col).color_token(turn_player, player_img(turn_player))
        game_board.one_square(row, col).draw(display)
        game_board.draw_board(display)
        pygame.display.flip()
        pygame.time.wait(100)
        game_board.one_square(r, col).color_token(0, empty_img)
        game_board.one_square(r, col).color_token(0)
        game_board.one_square(row, col).draw(display)
        pygame.display.flip()
        pygame.time.wait(20)
        game_board.draw_board(display)
        pygame.time.wait(20)
        pygame.display.flip()


# 1 = red -1 = blue
def rnd_player():
    if random.randint(0, 1) == 0:
        return 1
    return -1


def in_board(row, col):
    return 0 <= row < 6 and 0 <= col < 7


def check_is_win(row, col, val):
    if check_win(val, row, col, 0, -1) + check_win(val, row, col, 0, 1) > 2:
        return True
    if check_win(val, row, col, 1, 0) > 2:
        return True
    if check_win(val, row, col, -1, -1) + check_win(val, row, col, 1, 1) > 2:
        return True
    if check_win(val, row, col, -1, 1) + check_win(val, row, col, 1, -1) > 2:
        return True
    return False


def check_win(val, row, col, drow, dcol):
    count = -1
    while in_board(row, col) and game_board.one_square(row, col).val == val:
        row += drow
        col += dcol
        count += 1
    return count


if __name__ == '__main__':
        main()