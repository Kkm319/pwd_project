import random
import string

#strings for password generation

upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'
number='0123456789'
special='~!@#$%^&*_?'
all=upper+lower+number+special

pwd=[]
pwd.append(random.choice(upper))
pwd.append(random.choice(lower))
pwd.append(random.choice(number))
pwd.append(random.choice(special))

for i in range(4,12):
    pwd.append(random.choice(all))

random.shuffle(pwd)

passwords=''.join(pwd)
print(passwords)