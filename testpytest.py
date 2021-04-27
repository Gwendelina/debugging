import pytest
import random

def main():
    wallet_user = 100

    while wallet_user > 0 :
        #choice_user = input("Choisir une couleur : rouge ou noir ?) : ")
        choice_user = "rouge"
        while choice_user != "rouge" and choice_user != "noir" :
            print("Mauvaise couleur !")
            choice_user = input("Choisir une couleur (rouge ou noir) : ")

        #amount_user = int(input(f"Combien voulez-vous miser ? (Montant actuel : {wallet_user}€) : "))
        amount_user = wallet_user
        while amount_user > wallet_user :
            print('Montant insuffisant !')
            amount_user = int(input(f"Combien voulez-vous miser ? (Montant actuel : {wallet_user}€ : )"))

        random_number = random.randint(0, 36)
        print(f"La routellete est tombée sur {random_number} et votre couleur est : {choice_user}")
        
        if choice_user == "rouge" and random_number %2 == 0 : 
            wallet_user += amount_user
            print (f"Vous avez gagné {amount_user}€ ! Montant actuel : {wallet_user}€")
        elif choice_user == "noir" and random_number %2 == 1 :
            wallet_user += amount_user
            print (f"Vous avez gagné {amount_user}€ ! Montant actuel : {wallet_user}€")
        else :
            wallet_user -= amount_user
            print (f"Vous avez perdu {amount_user}€ ! Montant actuel : {wallet_user}€")

def ceciest():
    pass








main()