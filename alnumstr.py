import re
S=input()
m= re.search('(\w)(\d)', S)
if m:
  print("Yes")
else:
  print("No")
