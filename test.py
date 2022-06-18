import re

text = "The ghost that says boo haunts the loo"

m = re.findall("[bl]oo",text)

print(m)