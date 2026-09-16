import re

# scanner python file
def check_password(password):
    """
    Basic password security checker.
    """

    if len(password) < 8:
        return "Weak"

    if not re.search(r"[A-Z]", password):
        return "Weak"

    if not re.search(r"[a-z]", password):
        return "Weak"

    if not re.search(r"[0-9]", password):
        return "Weak"

    if not re.search(r"[^A-Za-z0-9]", password):
        return "Weak"

    return "Strong"
