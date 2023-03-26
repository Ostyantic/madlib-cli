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


def merge(string, tpl):
    return string.format(*tpl)


