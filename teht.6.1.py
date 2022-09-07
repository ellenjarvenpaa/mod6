import random

def heitäNoppaa():
    x = random.randint(1, 6)
    return x

while True:
    silmäluku = heitäNoppaa()
    print(silmäluku)
    if silmäluku == 6:
        break