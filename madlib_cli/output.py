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


def open_and_write(file_path):
    """

    :param file_path: The route of the file path
    :return: No Return
    """
    with open(file_path, 'w') as file:
        pass


def read_template(file_path):
    """
    Function that opens and reads a file template
    :param file_path: The route of the file path
    :return: The contents of the file as a string
    """
    with open(file_path, 'r') as file:
        # print(file.read())
        return file.read()


def get_descriptions(string):
    split_string = string.split()
    descriptors = []

    for i in range(len(split_string)):
        if "Adjective" in split_string[i]:
            descriptors.append("Adjective")
        elif "Noun" in split_string[i]:
            descriptors.append("Noun")

    descriptors = tuple(descriptors)
    print(descriptors)
    return descriptors


def parse_template(string):
    """
    Function that takes in a madlib string template,
    removes the contents of the user's
    selections and returns a new,
    hollowed copy for the user to fill out!
    :param string: madlib template
    :return: new madlib
    """
    descriptions = get_descriptions(string)
    mod_string = str()

    for item in descriptions:
        if not mod_string and str(item) in string:
            mod_string = string.replace(str(item), "")

        elif mod_string and str(item) in mod_string:
            mod_string = mod_string.replace(str(item), "")

    print(mod_string)
    # print(user_input)
    return mod_string


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


