# if order didn't matter could have used a set:
# my_set = set(string)
# vowels = frozenset("aeiou")
# final_str = ''.join(my_set.difference(vowels))

# because order matters keep a list

# Python code to remove all vowels from a string and keep chars in same order
def remove_vowels_keep_order(string):
    """
    :type string: str
    :rtype: str
    """
    # convert the string into a character list - wise so we can modify it
    char_list = []
    final_list = []
    result = " "
    char_list[:0] = string
    for char in char_list:
        if char in "aeiou":
            continue
        final_list.append(char)
    result = ''.join(final_list)
    return result

# Driver code
my_string = "momom"
print(remove_vowels_keep_order(my_string))


def remove_vowels(string):
    """
    :param string: str
    :return: str
    """
    char_list = []
    final_list = []
    result = " "
    char_list[:0] = string
    for char in char_list:
        if char in "aeiou":
            continue
        final_list.append(char)
    result = ''.join(final_list)
    return result

