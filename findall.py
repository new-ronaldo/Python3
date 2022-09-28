import re

x = "Привидение прошуршало и и исчезло в углу"

s = re.findall(".ло", x, re.IGNORECASE)

print(s)
