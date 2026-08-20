def calculate_search_space(length, charset_size):
    """
    Calculate total possible passwords.
    """
    return charset_size ** length


def estimate_time(search_space, guesses_per_second):
    """
    Estimate the time required.
    """
    return search_space / guesses_per_second


def convert_seconds(seconds):
    """
    Convert seconds into a readable format.
    """

    minute = 60
    hour = 60 * minute
    day = 24 * hour
    year = 365 * day

    if seconds < minute:
        return f"{seconds:.2f} seconds"

    elif seconds < hour:
        return f"{seconds/minute:.2f} minutes"

    elif seconds < day:
        return f"{seconds/hour:.2f} hours"

    elif seconds < year:
        return f"{seconds/day:.2f} days"

    else:
        return f"{seconds/year:.2f} years"