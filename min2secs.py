secret_number = 7
limit = 0

while limit < 3:
    u_num = int(input("Guess a Number btwn 1-10: "))
        
    if u_num == secret_number:
        print('You\'ve guessed right')
        break
   
    print('You are wrong! Try Again!!!')

    limit += 1
