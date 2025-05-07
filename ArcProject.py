import math as m

def arcForm(x):
    return m.sqrt(1 + (m.sin(x / 2) + (x / 2) * m.cos(x / 2)) ** 2)

total = 0

for j in range(28, 39):
    value = arcForm(j)
    print(f"x = {j}: {value}")
    total += value

print(f"\nTotal sum of arc values: {total}")
