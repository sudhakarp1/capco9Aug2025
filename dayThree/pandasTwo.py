import pandas as pd

s = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(s)
print(f'print s[0] : {s[4]}')
print(f'print s[b] : {s["b"]}')
