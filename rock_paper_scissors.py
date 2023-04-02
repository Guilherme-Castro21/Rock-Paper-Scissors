from random import choice

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


def is_win(player, opponent):
    # return true if player wins
    # rock > scissors, scissors > paper, paper > rock
    if (player == 'rock' and opponent == 'scissors') or \
            (player == 'scissors' and opponent == 'paper') or \
            (player == 'paper' and opponent == 'rock'):
        return True


while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower().strip()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    computer_pick = choice(options)
    print(f"Computer picked {computer_pick}.")

    if user_input == computer_pick:
        print("It's a tie!")
    elif is_win(user_input, computer_pick):
        print('You won!')
        user_wins += 1
    else:
        print('You lost!')
        computer_wins += 1

print(f'You won {user_wins} time(s).')
print(f'The computer won {computer_wins} time(s).')
