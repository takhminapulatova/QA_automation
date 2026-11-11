import pytest

class PasswordTooShortError(Exception):
    pass

def test_addition():
    result = 2 + 3
    assert result == 5

def test_subtraction():
    result = 2 - 3
    assert result == -1

def count_even_numbers(numbers):
    count_even = 0
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            count_even = count_even + 1
    return count_even

def test_count_even_numbers():
    assert count_even_numbers([2, 5, 8, 11, 14]) == 3
    assert count_even_numbers([1, 3, 5]) == 0
    assert count_even_numbers([]) == 0

def is_valid_password(password):
    if len(password) > 7:
        return True
    else:
        return False

def test_is_valid_password():
    assert is_valid_password("Password12345678") is True
    assert is_valid_password("Pass") is False
    assert is_valid_password("") is False
    assert is_valid_password("1234567") is False
    assert is_valid_password("12345678") is True
    assert is_valid_password("123456789") is True

@pytest.mark.parametrize('password, expected', [("Password12345678", True), ("Pass", False), ("", False), ("1234567", False), ("12345678", True), ("123456789", True)])
def test_with_parametrize(password, expected):
    assert is_valid_password(password) == expected

def multiply_numbers(*args):
    result = 1
    for i in args:
        result = result * i
    return result

def test_multiply_numbers():
    assert multiply_numbers(2, 3, 4) == 24
    assert multiply_numbers(5, 2) == 10
    assert multiply_numbers(3) == 3

def get_username(**kwargs):
    return kwargs["username"]

def test_get_username():
    assert get_username(username="tomsmith", age=30) == "tomsmith"
    assert get_username(username="admin", age=25) == "admin"

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Cannot divide by zero"

def validate_password(password):
    if len(password) < 8:
        raise PasswordTooShortError("Password too short")
    return True

def test_validate_password():
    assert validate_password("Password123") is True

    with pytest.raises(PasswordTooShortError) as error:
        validate_password("Pass")

    assert str(error.value) == "Password too short"

def test_custom_password_error():
    with pytest.raises(PasswordTooShortError) as error:
        validate_password("Pass")
