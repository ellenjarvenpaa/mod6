import random
tahkot = int(input("Kirjoita tahkojen määrä "))

def heitäNoppaa(tahkot):
    x = random.randint(1, tahkot)
    return x

while True:
    silmäluku = heitäNoppaa(tahkot)
    print(silmäluku)
    if silmäluku == tahkot:
        break