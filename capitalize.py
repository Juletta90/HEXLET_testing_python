
def capitalize(text):
    """ Функция, которая делает заглавной
    первую букву переданной строки """

    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'
