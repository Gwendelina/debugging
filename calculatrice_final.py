def ask_user(sentence = "Saisir un chiffre"): # askUser -> ask_user
    choice = input(f"""{sentence}\n>""")
    return choice

def addition(number): # Addition -> addition
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
            # print(list_numbers) -> créé ma liste
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers) # liste_numbers -> sum(list_numbers)
    return result

def multplication(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # ajout int 
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        #if index == '0': # do_something
        if index == 0:
            result = list_number
        else:
            #result = result / list_number # do_something
            result = result * list_number
    return result

def division(number):
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number)) # insert int
        number = ask_user("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for list_number, index in zip(list_numbers,list(range(len(list_numbers)))): # refactoriser
        if index == 0:
            result = list_number
        else:
            #result = result + list_number # do_something
            result = result / list_number
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit(): # ajouter ()
        if number.isdigit():
            list_numbers.append(int(number)) # ajout int 
        number = ask_user("Saisir un ciffre à additionner ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result

def display_interface():
    choice = ask_user("""
    Tu veux :
    1. Additionner Tape 1
    2. Soustraire Tape 2
    3. Multiplier Tape 3
    4. Diviser Tape 4""")
    while choice.isdigit():
        choice = int(choice) # insert int Pourquoi ? 
        if choice == 1:
            choice = ask_user("Saisir un ciffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(choice)
        elif choice == 2:
            choice = ask_user("Saisir un ciffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(choice)
        elif choice == 3:
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = multplication(choice)
        elif choice == 4:
            choice = ask_user("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = division(choice)
        return print(f"Le resultat est ==> {result}") 