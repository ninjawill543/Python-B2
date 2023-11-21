import random

nombres = []
for _ in range(100_000):
    # print(random.randint(1, 99) ** 2)
    nb = random.randint(1, 99) ** 2
    nombres.append(nb)
print(nombres)