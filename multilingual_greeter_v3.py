from typing import Dict
import random

# Steps to do:
# 1. Update greetings dictionary to lists - done
# 2. Update greet function - done
# 3. Update language_added function - done (not the most efficient way)
# 4. Update language_updated function
# 5. ? Update admin_mode - create option to select which greeting to change?





## Dictionaries

lang_dict = {
    1: 'English',
    2: 'Spanish'
}

name_prompt_dict = {
    1: 'What is your name?',
    2: 'Como te llamas?'
}

## updated the dictionary to the value being a list of 3 greetings ##
greetings_dict = {
    1: ['Hello', 'Good morning', 'Good afternoon'],
    2: ['Hola', 'Buenos días', 'Buenas tardes']
}


## General Functions

def print_language_options(lang_options: Dict[int, str]) -> None:
    print("Please choose a language: ")
    for key, value in lang_options.items():
        print(f'{key}: {value}')


def language_input() -> int:
    language_choice = input("Please select a language: ")
    return int(language_choice)


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    if lang_choice in lang_options.keys():
        return True
    else:
        return False


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    result = name_prompt_options.get(lang_choice)
    return result


def name_input(name_prompt: str) -> str:
    users_name = input(name_prompt)
    return users_name


## updated so that the greet function calls a random greeting from list in dictionary ##
def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    greetings_list = greetings_options.get(lang_choice)
    greetings_random = random.choice(greetings_list)
    print(greetings_random + " " + name)

## Main Welcome Screen

def admin_or_user():
    print("\nWelcome to the Multilingual Greeter")
    mode = (input("\nPlease select 'Admin' or 'User' mode: ")).lower()

    if mode == "admin":
        admin_mode()

    elif mode == "user":
        user_mode()

    else:
        print("Error, invalid mode selection")

    admin_or_user()

## Admin Mode

def admin_mode():
    print("\nYou are now in Admin mode.\n")
    print("Please select one of the following options:")
    print("1. Add support for additional languages")
    print("2. Update greetings for existing languages\n")
    mode_option = (input("Select: "))

    if mode_option == "1":
        language_added()

    elif mode_option == "2":
        language_updated()

    else:
        print("Error, invalid selection.")


## New Language [Admin Mode]

def language_added():

        ## New language inputs
        add_language = input("\nLanguage to be added: ")
        add_name_prompt = input("Name prompt for new language: ")
        add_greeting_one = input("First greeting for new language: ")
        add_greeting_two = input("Second greeting for new language: ")
        add_greeting_three = input("Third greeting for new language: ")

        ## 3 Greetings into a list
        add_greeting = []
        add_greeting.append(add_greeting_one)
        add_greeting.append(add_greeting_two)
        add_greeting.append(add_greeting_three)

        new_position = len(lang_dict)+1

        ## New dictionary key value pairs
        new_language = {new_position:add_language}
        new_name_prompt = {new_position:add_name_prompt}
        new_greeting = {new_position:add_greeting}

        ## Update existing dictionaries
        lang_dict.update(new_language)
        name_prompt_dict.update(new_name_prompt)
        greetings_dict.update(new_greeting)

        print("\nNew Language added: " + lang_dict[new_position] + "\n"
        "New Name Prompt added: " + name_prompt_dict[new_position] + "\n"
        "New Greeting added: " + str(greetings_dict[new_position]))

        #print("New language added: " + lang_dict[new_position])
        #print("New name prompt added: " + name_prompt_dict[new_position])
        #print("New greetings added: " + str(greetings_dict[new_position]))

## Update Language Greeting [Admin Mode]

def language_updated():

# To update language:
# 1. Print language options - done
# 2. Select language to update - done
# 3. Print current language greetings - done
# 4. Select update an existing  or  add a new element - done
# 5. If to update an existing greeting: - done
    # 5a. Select which greeting to update
    # 5b. Input new greeting
    # 5c. Function updates greeting
# 6. If to add a new greeting: - done
    # 6a. Input new greeting
    # 6b. Function to add greeting to existing list
# 7. Print updated greetings list - done

    print(lang_dict)
    update_language = int(input("Language to be updated: (Select a number) "))
    print(greetings_dict[update_language])
    print("1. Change an existing greeting\n"
          "2. Create an additional greeting\n")
    new_or_existing = int(input("Select a number: "))

    #Changing an existing greeting
    if new_or_existing == 1:
        which_greeting = input("Greeting to remove: ")
        i = greetings_dict[update_language].index(str(which_greeting))
        switched_greeting = input("Updated greeting: ")
        greetings_dict[update_language].pop(i)
        greetings_dict[update_language].append(str(switched_greeting))
        print("Updated greetings: " + str(greetings_dict[update_language]))


    #Adding a new greeting
    elif new_or_existing == 2:
        additional_greeting = input("Additional greeting to add: ")
        greetings_dict[update_language].append(str(additional_greeting))
        print("Updated greetings: " + str(greetings_dict[update_language]))

    else:
        print("Error, invalid selection.")


    ## PREVIOUS FUNCTION)
    #print(lang_dict)

    ##Language update input
    #update_language = int(input("Language to be updated: (Select a number) "))
    #greeting_update = str(input("Updated greeting: "))
    #greetings_dict.update({update_language:greeting_update})
    #print(greetings_dict)

## User Mode

def user_mode():
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)


if __name__ == '__main__':
    admin_or_user()