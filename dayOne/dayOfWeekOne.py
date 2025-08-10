dd, mm, yyyy = 8, 8, 2025

c, y = yyyy // 100 , yyyy % 100

week = int(dd + (2.6 * mm - 0.2) + y + y//4 + c // 4 - 2 * c) % 7
print(f'week value for {dd}-{mm}-{yyyy} is {week}')
