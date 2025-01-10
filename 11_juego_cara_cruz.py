import random
import os
os.system('cls')

print('--- JUEGO CARA O CRUZ ---')

cara_cruz = random.randint(1, 2)

if cara_cruz == 1:
    print('cara')
else:
    print('cruz')
