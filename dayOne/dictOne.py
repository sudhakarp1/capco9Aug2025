result = {0:0, 1:1}

def fiboList(num):
    if num not in result:
        result[num] = fiboList(num-1) + fiboList(num-2)
    return result[num]

num = 1000
for i in range(num):
    print(f'{i+1} --> {fiboList(i)}')
