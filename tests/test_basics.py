import pytest
@pytest.fixture

def numbers():
    return [2, 5, 8, 11, 14]
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
def test_is_even(numbers):
    assert is_even(4) is True
    assert is_even(9) is False
    assert is_even(-2) is True
    assert is_even(0) is True

def test_list_length(numbers):
    assert len(numbers) == 5

def test_even_numbers_from_list(numbers):
    assert is_even(2) is True
    assert is_even(numbers[0]) is True
    assert is_even(numbers[2]) is True

def test_odd_numbers_from_list(numbers):
    assert is_even(numbers[1]) is False

my_numbers = [2, 5, 8, 11, 14]

for num in my_numbers:
    if num % 2 == 0:
        print(num)

@pytest.mark.parametrize("num, expected", [(2, True), (5, False), (8, True)])
def test_even_parametrized(num, expected):
    assert is_even(num) == expected

def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

@pytest.fixture
def passwords():
    return ["abc", "password123", "hello123", "", "12345678"]

def test_passwords_from_list(passwords):
    assert is_valid_password(passwords[0]) is False
    assert is_valid_password(passwords[1]) is True
    assert is_valid_password(passwords[2]) is True

def test_passwords_with_loop(passwords):
    expected_results = [False, True, True, False, True]

    assert len(passwords) == len(expected_results)

    for password, expected in zip(passwords, expected_results):
        assert is_valid_password(password) == expected

    # for i in range(len(passwords)):
        # assert is_valid_password(passwords[i]) == expected_results[i]

@pytest.mark.parametrize("password, expected", [("hello123", True), ("hello12", False), ("", False), ("hello1234", True), ("hello1", False)])
def test_valid_password(password, expected):
    assert is_valid_password(password) == expected

@pytest.mark.parametrize("password, expected", [("1234567", False), ("12345678", True), ("123456789", True)])
def test_boundary_cases(password, expected):
    assert is_valid_password(password) == expected

def test_password_invalid_type():
    with pytest.raises(TypeError):
        is_valid_password(12345678)

def test_password_none():
    with pytest.raises(TypeError):
        is_valid_password(None)

@pytest.mark.parametrize("password, expected_error", [(123456789, TypeError), (None, TypeError), (3.14, TypeError)])
def test_invalid_passwords(password, expected_error):
    with pytest.raises(expected_error):
        is_valid_password(password)

def test_user_data():
    user = {
        "username": "tomsmith",
        "password": "hello123",
        "active": True
    }
    assert user["username"] == "tomsmith"
    assert user["active"] is True
    assert "password" in user
    assert "email" not in user

def test_user_profile():
    user = {
        "username": "tomsmith",
        "profile": {
            "city": "Austin",
            "active": True
        }
    }
    assert user["profile"]["city"] == "Austin"
    assert user["profile"]["active"] is True
