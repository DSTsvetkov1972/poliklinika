import os

folders = list(os.walk('Исходники'))[0][1]

m = max([len(f) for f in folders])


print(m)

for f in folders:
    print(f"{f:<{m}} { len(f) }")