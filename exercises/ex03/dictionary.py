"""Functions for ex03"""

__author__: str = "730656365"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """this function inverts the keys and values of a dictionary"""
    inverted_dict: dict[str, str] = dict()
    input_dict_keys: list[str] = []
    input_dict_values: list[str] = []
    i: int = 0
    for key in input_dict:
        input_dict_keys.append(key)
        input_dict_values.append(input_dict[key])
    if len(input_dict_values) != len(set(input_dict_values)):
        raise KeyError

    while i < len(input_dict):
        inverted_dict[input_dict_values[i]] = input_dict_keys[i]
        i = i + 1
    return inverted_dict


def count(count_list: list[str]) -> dict[str, int]:
    """this function creates a dictionary from a list that shows the count of times an item appears in the list"""
    count_dict: dict[str, int] = dict()
    i: int = 0
    while i < len(count_list):
        if count_list[i] in count_dict:
            count_dict[count_list[i]] += 1
        else:
            count_dict[count_list[i]] = 1
        i += 1
    return count_dict


def favorite_color(colors: dict[str, str]) -> str:
    """this function takes in a dictionary of people and their favorite colors and returns the most popular one"""
    list_of_colors: list[str] = []
    colors_counted: dict[str, int] = dict()
    popular_color: str = ""
    popular_color_count: int = 0
    for key in colors:
        list_of_colors.append(colors[key])
    colors_counted = count(list_of_colors)
    for key in colors_counted:
        if colors_counted[key] > popular_color_count:
            popular_color = key
            popular_color_count = colors_counted[key]
    return popular_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = dict()
    i: int = 0
    while i < len(words):
        if len(words[i]) not in bins:
            bins[len(words[i])] = {words[i]}
        else:
            bins[len(words[i])].add(words[i])
        i += 1
    return bins
