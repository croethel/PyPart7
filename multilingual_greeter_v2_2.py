from typing import Dict

## Dictionaries

lang_dict = {
    1: 'English',
    2: 'Spanish'
}

name_prompt_dict = {
    1: 'What is your name?',
    2: 'Como te llamas?'
}

greetings_dict = {
    1: 'Hello',
    2: 'Hola'
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


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    result = greetings_options.get(lang_choice)
    print (result + " " + name)

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
        add_greeting = input("Greeting for new language: ")

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
        "New Greeting added: " + greetings_dict[new_position] + "\n")


## Update Language Greeting [Admin Mode]

def language_updated():

    print(lang_dict)

    ##Language update input
    update_language = int(input("Language to be updated: (Select a number) "))
    greeting_update = str(input("Updated greeting: "))
    greetings_dict.update({update_language:greeting_update})
    print(greetings_dict)

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