Players = ['alex', 'antu', 'vureui', 'crerent', 'tob']

import random
# def battleRoyale():
#     for player in list(Players):
#         eleminate = Players.pop(random.randrange(len(Players)))
#     print(f'{eleminate} was eliminated')
#     print(Players)
# battleRoyale()
# eleminate = Players.pop(random.randrange(len(Players)))
# print(f'{eleminate} was eliminated')

for player in list(Players):

    if len(Players) > 1:
        eliminate = Players.pop(random.randrange(len(Players)))
        print(f'{eliminate} was eliminated')
    elif len(Players) == 1:
        print(*Players, 'won')

