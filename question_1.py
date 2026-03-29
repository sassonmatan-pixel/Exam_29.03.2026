count = 0
user_grade = None
list1 = []
while True:
    user_grade = input(f"Enter your grade:")
    try:
        user_grade = int(user_grade)
    except ValueError:
        print("Invalid input, skip")
        continue
    except TypeError:
        print("Invalid input, skip")
        continue

    if user_grade != -999:
        if user_grade < 0 or user_grade > 100:
            print("skip big or small number")
        else:
            list1.append(user_grade)


    elif len(list1) >= 10:
        print(f'the avg is:{sum(list1)/len(list1)}')
        print(f'the max is:{max(list1)}')
        print(f'the valid input is:{len(list1)}')
        break

    else:
        print('Need at least 10 valid grades. Keep entering.')

