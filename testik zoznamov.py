zoz = []
import random
for i in range (10):
    zoz.append(random.randrange(1,101))
print(zoz)


zoz_pa = 0
zoz_pa_idx = 0
for i in range (len(zoz)):
    if zoz[i] % 2 == 0:
        zoz_pa += zoz[i]
    if i % 2 == 0:
        zoz_pa_idx += zoz[i]
print(zoz_pa, zoz_pa_idx)