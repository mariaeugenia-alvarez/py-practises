from src.geometric_sequence import geometric_sequence_sum
from src.geometric_sequence import calculateComplexCase

""" def test_geometric_sequence_sum():
    # Arrange
    a, r, n = 2, 3, 4
    esperado = 80  # 2 * (3^4 - 1) / (3 - 1)
    # Act
    resultado = geometric_sequence_sum(a, r, n)
    # Assert
    assert resultado == esperado """

def test_calculateComplexCase():
    # Test case 1
    assert calculateComplexCase(2, 3, 5) == 242  # 2 * (3^5 - 1) / (3 - 1)
    # Test case 2
    # Test case 3
    assert calculateComplexCase(2, 2, 10) == 2046  # 2 * (2^10 - 1) / (2 - 1)
    # Test case 4
    assert calculateComplexCase(1, -2, 10) == -341  # Alternating series
    # Test case 5
    assert calculateComplexCase(1, 0.5, 10) == 1.998046875  # Fractional ratio

def test_geometric_sequence_sum_example_tests():
    # Test case 1
    assert geometric_sequence_sum(2, 3, 5) == 242  # 2 * (3^5 - 1) / (3 - 1)
    # Test case 2
    assert geometric_sequence_sum(1, 1, 2) == 2  # 1 * 2
    # Test case 3
    assert geometric_sequence_sum(2, 2, 10) == 2046  # 2 * (2^10 - 1) / (2 - 1)
    # Test case 4
    assert geometric_sequence_sum(1, -2, 10) == -341  # Alternating series
    # Test case 5
    assert geometric_sequence_sum(1, 0.5, 10) == 1.998046875  # Fractional ratio