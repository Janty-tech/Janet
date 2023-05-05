#while loop syntax:

for element in sequence:
    #for statement code block
else: # optional
    #else block code

...
from random import Random


def change_count():
    global count
    r = Random()
    cont = r.randint(0, 12)


count = 0
while count < 10:
    print("print this random times")
    change_count()
