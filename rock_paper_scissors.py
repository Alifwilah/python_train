import utils
import random

print("Start rock paper scissors game")
player_name = input("Enter your name: ")

print("Choose hand: (0: Rock, 1: Paper, 2: Scissor)")
player_hand = int(input("Input number (0-2): "))

if utils.validate(player_hand):
    computer_hand = random.randint(0,2)

    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')

    result = utils.judge(player_hand, computer_hand)
    print('Result ' + result)
else:
    print("Enter the correct number")
