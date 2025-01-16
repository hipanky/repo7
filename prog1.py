import re

s1='He is good boy 17 Years old & he live in Delhi'

res=re.findall(r'\d',s1)

for i in res:
    print(i)
    

