def find_median(numbers: list) -> float:
    """
    This function find the median of numbers
    :param numbers: is user input numbers
    :return: the median of numbers
    """
    numbers.sort()

    #This is checkin if the numbers on the list is odd or even
    #for even numbers
    if len(numbers) % 2 == 0:
        right_median = numbers[len(numbers) // 2]
        left_median = numbers[len(numbers) // 2 - 1]
        return (right_median + left_median) / 2

    #for odd numbers
    else:
        return float(numbers[len(numbers) // 2])

#example printing
numbers = [3, 1, 4, 1, 5]
print(find_median(numbers))

numbers = [7, 2, 9, 10]
print(find_median(numbers))

numbers = [42]
print(find_median(numbers))