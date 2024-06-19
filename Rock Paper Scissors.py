#Rock Paper Scissors
import random
op=['rock','paper','scissors']


while True:
    while True:
        user= input('Choose(rock, paper, scissors):')
        if user not in op:
            print('invalid')
            continue

        bot=random.choice(op)
        print('Computer choice:',bot)

        if user==bot:
            print('Its a tie,Try Again')
        elif ((user=='rock' and bot=='scissors') or (user=='paper' and          bot=='rock') or (user=='scissors' and bot=='paper')) :
            print('Victory!')
            break
        else:
            print('Defeated \nTry Again')

    print('Congratulations! You won!')
    play_again=input("Do you want to continue? (yes/no):").lower()
    if play_again!="yes":
        break
print('Thank you for playing')
