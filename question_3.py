def snake_to_camel(text: str) -> str:
    """
    This function convert snake to camel
    :param text: text is the user's input
    :return: str
    """
    x = 0 # the item 'x' is for pass the value '_'
    new_text = ''
    for letter in text:
        if letter == '_':
            x = 1
            pass

        elif x == 0: # if no see the value '_'
            new_text += letter

        else:
            new_text += letter.upper() #after I see the value '_' the next value is big
            x = 0

    return new_text


text1: str ='hello_python'
print(snake_to_camel(text1))
text2: str ='my_variable_name'
print(snake_to_camel(text2))
text3: str ='python'
print(snake_to_camel(text3))
text4: str ='a_b_c_d'
print(snake_to_camel(text4))
