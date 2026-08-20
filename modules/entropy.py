import math
import re


def detect_charset(password):
    """
    Estimate the size of the character set used by the password.
    """

    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26

    if re.search(r"[A-Z]", password):
        charset += 26

    if re.search(r"\d", password):
        charset += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    return charset


def calculate_entropy(password):

    charset = detect_charset(password)
    length = len(password)

    if charset == 0 or length == 0:
        return 0, "Very Weak"

    entropy = length * math.log2(charset)

    if entropy < 28:
        rating = "Very Weak"
    elif entropy < 36:
        rating = "Weak"
    elif entropy < 60:
        rating = "Reasonable"
    elif entropy < 128:
        rating = "Strong"
    else:
        rating = "Very Strong"

    return round(entropy, 2), rating