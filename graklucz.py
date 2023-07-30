from math import sqrt
from random import randint

game_width = 10
game_height = 10

key_x = randint(0, game_width)
key_y = randint(0, game_height)
player_x = 0
player_y = 0
player_found_key = False
#ilosć ruchów
steps = 0
#dystans pomiędzy graczem, a skarbem przed
distance_before_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)


while not player_found_key:
    steps += 1
    print()
    print('Możesz udać się w kierunkach określonych jako [W/A/S/D]: ')

    move = input('Dokąd idziesz?')
    match move.lower():
        case 'w':
            player_y += 1
            if player_y > game_height:
                print('Uderzasz w ścianę!!!')
                player_y = game_height
        case's':
            player_y -= 1
            if player_y < 0:
                print('Uderzasz w ścianę!!!')
                player_y = 0

        case 'a':
            player_x -= 1
            if player_x < 0:
                print('Uderzasz w ścianę!!!')
                player_x = 0
        case 'd':
            player_x += 1
            if player_x > game_width:
                print('Uderzasz w ścianę!!!')
                player_x = game_width
        case 'q':
            quit('Koniec gry!!!')
        case '_':
            print('Nie wiem dokąd idziesz...')
            continue

    if player_x == key_x and player_y == key_y:
        print('Klucz jest Twój!!!')
        print(f'Wykonałeś/aś {steps} ruchów.')
        quit()

     #dystans pomiędzy graczem, a skarbem po
    distance_after_move = sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)

    if distance_before_move > distance_after_move:
        print('Zbliżasz się do klucza')
    else:
        print('Oddalasz się od klucza :(')

    distance_before_move = distance_after_move






