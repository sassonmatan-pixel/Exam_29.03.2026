import string
def most_common_word(story: tuple[str, ...]) -> str:
    """
    This function returns the most common word
    :param story: get story from the user
    :return: str
    """
    list1 = []
    dict1 = {}
    for sentence in story:
        words = sentence.split()
        for word in words:
            word = word.lower()
            for punctuation in string.punctuation:
                word = word.replace(punctuation,  '')
            list1.append(word)
    set1 = set(list1.copy())
    for word in set1:
        dict1[word] = list1.count(word)
    print(dict1)
    return f"{max(dict1, key=lambda k: dict1[k])} is {dict1[max(dict1, key=lambda k: dict1[k])]} times"

story = (
    "The little fox saw the little bird and the little cat.",
    "The fox was happy because the little bird sang, and the little cat jumped.",
    "The little fox, the little bird, and the little cat became friends."
)

is_double_word = most_common_word(story)
print(is_double_word)