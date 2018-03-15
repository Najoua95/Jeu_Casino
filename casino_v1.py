from random import randrange
import time
# VERSION 1
# Define computer's choice
def score_comp (start = 0, stop = 49, step = 1) :
    nb_alea = randrange(0, 49, 1)
    return nb_alea

# Check if player's number includes the correct values
def check_nb_user (nb_user) :
    if (nb_user > 0 and nb_user < 49) :
        return True
    else :
        return False

# Check that the player has enough money
def check_bet_user (bet_user, money) :
    if (bet_user > money) :
        print('You dont have enought money')
        return False
    if (bet_user < 1) :
        print('Your bet is negative or null')
        return False
    else :
        return True

# Control exception - player number
def check_tape_nb_user ():
    while True :
        try :
            nb_user = int(input('Please, Choose your number : '))
            break
        except ValueError :
            print('You have to type a number !')
    return nb_user

# Control exception - player bet
def check_tape_bet_user ():
    while True :
        try :
            bet_user = int(input('What is your bet ? : '))
            break
        except ValueError :
            print('You have to type a number')
    return bet_user

# Define conditions when player win or game over
money = 200
def cash (money, bet_user, nb_alea):
    if nb_alea == bet_user :
        print('No more bets : let\'s hunt ! \nThe roulette wheel spins...')
        time.sleep(2)
        print('My choice : ', nb_alea)
        print('Congrats ! You win three times your bet !')
        print('You win {} euros !'.format(bet_user*3))
        money = money + (bet_user*3)
        print('You have {} euros !'.format(money))
        return money
    if nb_alea %2 == bet_user %2 :
        print('No more bets : let\'s hunt ! \nThe roulette wheel spins...')
        time.sleep(2)
        print('My choice : ', nb_alea)
        print('Not to bad, you found the same color ! You win half of your bet !')
        print('You win {} euros !'.format(int(bet_user/2)))
        money = money + (int(bet_user/2))
        print('You have {} euros !'.format(money))
        return money
    else :
        print('No more bets : let\'s hunt ! \nThe roulette wheel spins...')
        time.sleep(2)
        print('My choice : ', nb_alea)
        print('Game Over !')
        money = money - bet_user
        return 0

# Launching Casino Game
def game() :
    print('Hello Buddy ! \nWelcome to Naj Casino ! \nPlace your bet !')
    money = 200
    answer = 'yes'
    while answer == 'yes' and money > 0:
        while True :
            nb_user = check_tape_nb_user ()
            if (check_nb_user(nb_user) == True ):
                break
            else :
                print('Wrong value ! You have to choose a number between 0 and 49')
        while True :
            bet_user = check_tape_bet_user ()
            if (check_bet_user(bet_user, money) == True ):
                break

        money = cash(money, bet_user, score_comp())

        while True :
            answer = input('Do you want to bet again ? : yes or no : ')
            if answer == "yes" and money > 0:
                print('Good Luck, Buddy !')
                break
            if answer == "yes" and money < 1:
                print('No more money ! \nGood Bye !\nCome back to bet anytime, Buddy !')
                break
            else :
                print('Good Bye !\nCome back to bet anytime, Buddy !')
                break
game()



