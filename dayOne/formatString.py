num, name, price = 100, 'Krack Jack', 23.34
resString='Id: {} name: {}  Price: {}'.format(num, name, price)
print(resString)

resString='Id: {0} name: {1}  Price: {2}'.format(num, name, price)
print(resString)
resString='{1}  {0}  {2}'.format(num, name, price)
print(resString)
resString='{2}  {0}  {1}'.format(num, name, price)
print(resString)
resString='{1}  {2}  {0}'.format(num, name, price)
print(resString)
resString='{2}  {1}  {0}'.format(num, name, price)
print(resString)


