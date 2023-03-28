import re


def open_and_read(file_path):
    """
    A function that takes in the file's path as a parameter.
    The file passed through is opened and read to the terminal.
    :param file_path: the route
    :return: A string of the file
    """
    with open(file_path, 'r') as file:
        print(file.read())
        return file.read()


def open_and_write(file_path, string):
    """
    Function that opens and writes to a file path
    :param file_path: The route of the file path
    :param string: String to write in file
    :return: No Return
    """
    with open(file_path, 'w') as file:
        # print(file.write(string))
        file.write(string)


def read_template(file_path):
    """
    Function that opens and reads a file template
    :param file_path: The route of the file path
    :return: The contents of the file as a string
    """
    with open(file_path, 'r') as file:
        # print(file.read())
        return file.read()


# def get_descriptions(string):
#     split_string = string.split()
#     descriptors = []
#
#     for i in range(len(split_string)):
#         if "Adjective" in split_string[i]:
#             descriptors.append("Adjective")
#         elif "Noun" in split_string[i]:
#             descriptors.append("Noun")
#
#     descriptors = tuple(descriptors)
#     print(descriptors)
#     return descriptors


def parse_template(string):
    """
    Function that takes in a madlib string template,
    removes the contents of the user's
    selections and returns a new,
    hollowed copy for the user to fill out!
    :param string: madlib template
    :return: new madlib
    """
    descriptions = get_placeholders(string)
    mod_string = str()

    for item in descriptions:
        if not mod_string and str(item) in string:
            mod_string = string.replace(str(item), "")

        elif mod_string and str(item) in mod_string:
            mod_string = mod_string.replace(str(item), "")

    # print(mod_string)
    # print(user_input)
    return mod_string, descriptions


def merge(string, tpl):
    """
    Function that takes in a string and a tuple or list
    of strings, and formats the tuple or list into the string.
    :param string: A string
    :param tpl: A tuple OR list
    :return: modified string
    """
    mod_string = string.format(*tpl)

    return mod_string


def get_placeholders(string):
    """
    Function that takes in a string, finds any placeholder text
    in the string and creates a set of those placeholder.
    :param string: A string with placeholders.
    :return: A set of placeholder items.
    """

    pattern = r'{(.*?)}'
    placeholders = tuple(re.findall(pattern, string))
    # placeholders = tuple(placeholders)

    return placeholders


def get_user_selection(tpl):
    """
    Function that takes a tuple of descriptions,
    iterates over the tuple and gets the input
    :param tpl:
    :return: A tuple of user input
    """
    users_words = []
    for item in tpl:
        users_words.append(input(f"Please enter a {str(item)}: "))

    users_words = tuple(users_words)
    # print(users_words)
    return users_words


