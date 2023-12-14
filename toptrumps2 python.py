import random
import requests
import time


def your_turn():
    number_selection = input("Pick a number between 1 and 82: ")
    url = "https://swapi.dev/api/people/{}".format(number_selection)
    your_response = requests.get(url)
    your_sw_character = your_response.json()
    return dict(name=your_sw_character['name'], height=your_sw_character['height'], mass=your_sw_character['mass'])


def computer_turn():
    random_sw_id = random.randint(1, 82)
    url = "https://swapi.dev/api/people/{}".format(random_sw_id)
    computer_response = requests.get(url)
    computer_sw_character = computer_response.json()
    return dict(name=computer_sw_character['name'], height=computer_sw_character['height'], mass=computer_sw_character['mass'])


def game():
    user_score = 0
    computer_score = 0
    winning_score = int(input("You will play rounds with your opponent until one of you wins.  How many points is your goal?"))
    while user_score < winning_score and computer_score < winning_score:
        your_sw_character = your_turn()
        print('Your stats are - name:{}, mass:{}, height:{}'.format(your_sw_character['name'], your_sw_character['mass'], your_sw_character['height']))
        computer_sw_character = computer_turn()
        time.sleep(2)
        print("The computer picked {}".format(computer_sw_character["name"]))
        time.sleep(2)
        print("\n")
        your_selection = input("Please pick the height or mass: ")
        time.sleep(2)
        print("The computer {} is {}".format(your_selection, computer_sw_character[your_selection]))
        print("Your {} is {}".format(your_selection, your_sw_character[your_selection]))
        time.sleep(2)


        if your_sw_character[your_selection] == "unknown":
            your_sw_character[your_selection] = 0

        if computer_sw_character[your_selection] == "unknown":
            computer_sw_character[your_selection] = 0


        time.sleep(1)
        print("\n")

        if float(computer_sw_character[your_selection]) == float(your_sw_character[your_selection]):
            print("You draw")
        elif float(computer_sw_character[your_selection]) > float(your_sw_character[your_selection]):
            computer_score = computer_score + 1
            print('Computer wins! Your Score: {}'.format(user_score), 'Computer Score: {}'.format(computer_score))
        else:
            user_score = user_score + 1
            print('You win! Your Score: {}'.format(user_score), 'Computer Score: {}'.format(computer_score))


    if user_score or computer_score == winning_score:
        print("\n")
        print('Game Over!')
        play_again_answer = input('Do you want to play again? (Y/N)')
        if play_again_answer == 'Y':
            game()
        elif play_again_answer =='N':
            print('Bye!')

game()
