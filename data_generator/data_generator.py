import random
import string

def generate_string(length, content):
    """
    Generate a string of specified length and content.

    Args:
        length (int): Length of the string to be generated.
        content (str, optional): Content of the string. Options are "same_char", "diff_chars", "random", or "enumeration_example". Defaults to "random".

    Returns:
        str: Generated string.
    """
    if content == "same_char":
        return "a" * length
    elif content == "diff_chars":
        alphabet = string.ascii_lowercase
        result = ""
        while len(result) < length:
            result += alphabet + alphabet[::-1]
        return result[:length]
    elif content == "random":
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    elif content == "enumeration":
        palindrome_sequence = "az"
        result = palindrome_sequence * ((length // len(palindrome_sequence)) + 1)
        return result[:length]
    else:
        raise ValueError("Invalid value for 'content'. Please choose from 'same_char', 'diff_chars', 'random', or 'enumeration_example'.")
