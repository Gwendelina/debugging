import pytest
import random


wallet_user = 100

def choise_color_user():
    choice_user = "noir"
    return choice_user
    
def lol():
    pass

def choise_amount_user(wallet_user):
    amount_user = 10
    assert amount_user <= wallet_user
    #assert amount_user > wallet_user
    while amount_user > wallet_user :
        print('Montant insuffisant !')
        amount_user = wallet_user
    return amount_user


def random_number_roulette(choice_user):
    random_number = random.randint(0, 36)
    print(f"La routellete est tombée sur {random_number} et votre couleur est : {choice_user}")
    return random_number


def calculs(wallet_user, choice_user, random_number):
    if random_number == 0 :
        wallet_user -= amount_user
        print (f"Vous avez perdu {amount_user}€ ! Montant actuel : {wallet_user}€")
    elif choice_user == "rouge" and random_number %2 == 0 : 
        assert choice_user == "rouge" and random_number %2 == 0
        wallet_user += amount_user
        print (f"Vous avez gagné {amount_user}€ ! Montant actuel : {wallet_user}€")
    elif choice_user == "noir" and random_number %2 == 1 :
        wallet_user += amount_user
        print (f"Vous avez gagné {amount_user}€ ! Montant actuel : {wallet_user}€")
    else :
        wallet_user -= amount_user
        print (f"Vous avez perdu {amount_user}€ ! Montant actuel : {wallet_user}€")
    return wallet_user


def test_choice_color():
    assert choice_user == "rouge" or choice_user == "noir"

# while wallet_user > 0 :
#     choice_user = choise_color_user()
#     amount_user = choise_amount_user(wallet_user)
#     random_number = random_number_roulette(choice_user)
#     wallet_user = calculs(wallet_user, choice_user, random_number)

def salut():
    return 42

print(salut())