import re
str = '''
navid@gmail.com
nasdha
iwi
elliot_alderson@co.in
565
mr.robot9@yahoo.in
hello world
minombreeselliotalderson777@elliot.com
'''

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+", str)
print(email)
for items in email:
    print(items)

