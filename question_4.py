list_with_dupy = []
set_list_with_dupy = []

while True:
    text_user = input('Enter a string: ')
    text_user = text_user.strip()
    text_user = text_user.lower()
    if text_user == 'quit':
        set_list_with_dupy = list_with_dupy.copy()
        set_list_with_dupy = set(set_list_with_dupy)
        break

    else:
        list_with_dupy.append(text_user)

if len(set_list_with_dupy) == len(list_with_dupy):
    print('\nThere were no duplicates')

else:
    print('\nThere were duplicates')

