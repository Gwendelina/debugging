#kfdkfhgk
def askUser(sentence = "Saisir un chiffre"): # do_something
    choice = input(f"""{sentence}\n>""")
    return choice


def addition(number): # do_something
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
            # print(list_numbers)
            # print(type(list_numbers))
            # print(len(list_numbers))
        number = input("Saisir un ciffre à additionner ou clicker sur '=' ")
    result = sum(list_numbers) # do_something
    return result

def multplication(number):
    result = 1
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = input("Saisir un ciffre à multiplier ou clicker sur '=' ")
    for element in list_numbers:
        #if element == 0:
        #    pass 
        #else: 
        result *= element
    return result

def division(number):
    result = 1
    list_numbers = []
    while number.isdigit():
        if number.isdigit():
            list_numbers.append(int(number))
        number = input("Saisir un ciffre à additionner ou clicker sur '=' ")
    for element in list_numbers:
        print(f"{result} / {element}")
        result = result / element
        
    return result

def soustraction(number):
    list_numbers = []
    while number.isdigit: # do_something
        if number.isdigit():
            list_numbers.append(number) # do_something
        number = input("Saisir un ciffre à additionner ou clicker sur '=' ")
    i = 0
    for list_number in list_numbers:
        if i == 0:
            result = list_number
        else:
            result = result - list_number
        i = i + 1
    return result

def display_interface():
    choice = "0"
    while choice.isdigit():
        choice = input("""
        Tu veux :
        1. Additionner Tape 1
        2. Soustraire Tape 2
        3. Multiplier Tape 3
        4. Diviser Tape 4 \n""")
        choice = choice # do_something
        if choice == "1":
            number = input("Saisir un ciffre à ADDITIONNER ou clicker sur '=' ")
            result = addition(number)

        elif choice == "2":
            number = input("Saisir un ciffre à SOUSTRAIRE ou clicker sur '=' ")
            result = soustraction(number)
        elif choice == "3":
            number = input("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = multplication(number)
        elif choice == "4":
            number = input("Saisir un ciffre à MULTIPLIER ou clicker sur '=' ")
            result = division(number)
        print(f"Le resultat est ==> {result} ")


