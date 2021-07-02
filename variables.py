import random

nos = []

for i in range(2):
    choice = random.randrange(1,10)

    if choice not in nos:
        nos.append(choice)
    

print(nos)