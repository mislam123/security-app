from app.scanner import check_password


def test_weak_password():
    assert check_password("hello") == "Weak"


def test_missing_number():
    assert check_password("Password!") == "Weak"


def test_missing_uppercase():
    assert check_password("password123!") == "Weak"


def test_strong_password():
    assert check_password("Password123!") == "Strong"

