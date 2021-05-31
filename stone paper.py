from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move =randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    print(computer_choice)

    if player_choice == computer_choice:
        print ('choose your option')
    elif player_choice == 'rock' or computer_choice == 'scissors':
        win()
        # print("you chose rock and computer chose paper, you win ")
    elif player_choice == 'paper' or computer_choice == 'scissors':
        lose()
        # print("you chose paper and computer chose scissors,you lose ")
    elif player_choice == 'scissors' or computer_choice == 'paper':
        win()
        # print("you chose scissors and computer chose paper,you win")
    elif player_choice == 'scissors' or computer_choice == 'rock':
        lose()
        # print("you chose scissors and computer chose rock ,you lose")
    elif player_choice == 'paper' or computer_choice == 'rock':
        lose()
        # print("you chose paper and computer chose rock, you lose")
    elif player_choice =='rock' or computer_choice =='paper' :
        # print("you chose rock and computer chose paper, you win")
        win()
    again = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break 