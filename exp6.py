import re

txt='There is rain in Spain in the plain.'
x=re.sub('Spain','brain',txt)
print(txt)
print(x)
y=re.search('ain',txt)
print(y)
z=re.findall(r'ain\b',txt)
print(z)
q=re.findall('[ain]',txt)
x = re.findall("\w", txt)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
x = re.split("\s", txt, 1)
print(x)
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
