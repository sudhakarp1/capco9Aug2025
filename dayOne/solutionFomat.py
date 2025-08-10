lst = [(100, 'Krack Jack', 23.34), (101,'Jim Jam',35.5), 
       (102, 'Little Hearts',48.0), (103,'Treat', 37.5)]
qty = [0, 4, 7, 2]
print('-' * 48)
print('%-5s%-5s%-15s%-6s%-8s%8s' % ('SlNo','PId','Name','Qty','Price','Amt'))
print('-' * 48)
cnt, sum = 1, 0.0
for i in range(len(lst)):
    if qty[i] != 0:
        amt = qty[i] * lst[i][2]
        print('%-5d%-5d%-15s%-6d%-8.2f%8.2f' % (cnt, lst[i][0], lst[i][1], qty[i], lst[i][2], amt))
        sum += amt
        cnt+=1
print('-' * 48)
print('%38s%8.2f' % ('Total: ',sum))
print('-' * 48)