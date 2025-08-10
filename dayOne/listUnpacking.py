x, y, z = 10, 20, 30
print(f'x: {x}  y: {y}  z: {z}')

x, y, *z = 10, 20, 30, 40, 50
print(f'x: {x}  y: {y}  z: {z}')

x, *y, z = 10, 20, 30, 40, 50
print(f'x: {x}  y: {y}  z: {z}')

*x, y, z = 10, 20, 30, 40, 50
print(f'x: {x}  y: {y}  z: {z}')

x, y, *z = 40, 50
print(f'x: {x}  y: {y}  z: {z}')
