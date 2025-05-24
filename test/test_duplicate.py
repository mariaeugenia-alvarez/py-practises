from src.duplicate.solution import solution

def test_solution():
    # Test case 1
    assert solution('adTA34hnA4') == 2  # 'a' and '4' appear twice
    # Test case 2
    assert solution('aA') == 1  # 'a' appears twice, case insensitive
    # Test case 3
    assert solution('abc') == 0  # No characters repeat
    # Test case 4
    assert solution('') == 0  # Empty string
    # Test case 5
    assert solution('1234567890') == 0  # No characters repeat
    # Test case 6
    assert solution('aaAA') == 1  # 'a' appears four times, case insensitive
    # Test case 7
    assert solution('!@#$%^&*()_+') == 0  # No characters repeat
