from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: 'English',
    2: 'Spanish'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
    1: 'What is your name?',
    2: 'Como te llamas?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
    1: 'Hello',
    2: 'Hola'
}


def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for key, value in lang_options.items():
        print(f'{key}: {value}')


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    language_choice = input("Please select a language: ")
    return int(language_choice)



def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    if lang_choice in lang_options.keys():
        return True
    else:
        return False


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    result = name_prompt_options.get(lang_choice)
    return result



def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    users_name = input(name_prompt)
    return users_name

def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    result = greetings_options.get(lang_choice)
    print (result + " " + name)


def admin_or_user():
    print("Welcome to the Multilingual Greeter")
    mode = (input("\nPlease select 'Admin' or 'User' mode: ")).lower()

    ##Admin Mode
    if mode == "admin":

        print("\nYou are now in Admin mode.\n")
        print("Please select one of the following options:")
        print("1. Add support for additional languages")
        print("2. Update greetings for existing languages\n")
        mode_option = (input("Select: "))

        ##Additional languages
        ##Language, name prompt, greeting
        if mode_option == "1":

            ##New language inputs
            add_language = input("\nLanguage to be added: ")
            add_name_prompt = input("Name prompt for new language: ")
            add_greeting = input("Greeting for new language: ")

            new_position = len(lang_dict)+1

            ##New dictionary key value pairs
            new_language = {new_position:add_language}
            new_name_prompt = {new_position:add_name_prompt}
            new_greeting = {new_position:add_greeting}

            ##Update existing dictionaries
            lang_dict.update(new_language)
            name_prompt_dict.update(new_name_prompt)
            greetings_dict.update(new_greeting)

            print("\nNew Language added: " + lang_dict[new_position] + "\n"
            "New Name Prompt added: " + name_prompt_dict[new_position] + "\n"
            "New Greeting added: " + greetings_dict[new_position] + "\n")

        ##Update greetings
        ##Which language?
        ##What should greeting be updated to?
        #Then update dictionary

        elif mode_option == "2":
            print(lang_dict)

            ##Language update input
            update_language = int(input("Language to be updated: (Select a number) "))
            greeting_update = str(input("Updated greeting: "))
            greetings_dict.update({update_language:greeting_update})
            print(greetings_dict)

        ##Error
        else:
            print("Error, invalid selection.")

    ##User Mode
    elif mode == "user":
        pass

    #Error
    else:
        print("Error, invalid mode selection")



admin_or_user()

if __name__ == '__main__':
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)