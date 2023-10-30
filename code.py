import random 

print("Let's play Rock Paper Scissors")

def play():
    user = input("What\'s your choice 'r' for Rock, 'p' for Paper, 's' for scissors\n")
    computer = random.choice(['r','p','s'])

    if user == 'q':
        return 'Quit'
    
    if user in (['r', 's', 'p']):
        if user == 'r':
            print('You chose Rock')
        elif user == 'p':
            print('You chose Paper')
        elif user == 's':
            print('You chose Scissor')
        
        if computer == 'r':
            print('Computer chose Rock')
        elif computer == 'p':
            print('Computer chose Paper')
        elif computer == 's':
            print('Computer chose Scissor')
        
    
        if user == computer:
            return 'It\'s a tie'

        if is_win(user, computer):
            return 'You won'
        
        return 'You lost'
    
    else:
        print('Invalid input!! Please choose r for Rock, s for Scissors or P for Paper')
        exit()

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
while True:
    result = play()
    if result == 'Quit' or result == 'You lost':
        print(result)
        break
    else:
        print(result)