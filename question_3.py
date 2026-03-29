def snake_to_camel(text: str) -> None:
    """
    This function convert snake to camel
    :param text: text is the user's input
    :return: None
    """
    x = 0
    for letter in text:
        if letter == '_':
            x = 1
            pass

        elif x == 0:
            print(letter, end='')

        else:
            print(letter.upper(), end='')


text1: str ='a_b_c'
snake_to_camel(text1)
