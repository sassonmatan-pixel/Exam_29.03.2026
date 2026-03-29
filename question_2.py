def find_median(numbers: list) -> float:
    """
    This function find the median of numbers
    :param numbers: is user input numbers
    :return: the median of numbers
    """
    numbers.sort()
    if len(numbers) % 2 == 0:
        return numbers[(len(numbers) // 2 -1)] + numbers[len(numbers) // 2]

    else:
        return numbers[len(numbers) // 2]

numbers = [4, 3, 2, 1, 5]
print(find_median(numbers))

numbers = [4, 3, 2, 1]
print(find_median(numbers))

numbers = [42,]
print(find_median(numbers))