from src.geometric_sequence.solution import solution

def test_solution():
    # Test case 1
    assert solution(2, 3, 5) == 242  # 2 * (3^5 - 1) / (3 - 1)
    # Test case 2
    assert solution(1, 1, 2) == 2  # 1 * 2
    # Test case 3
    assert solution(2, 2, 10) == 2046  # 2 * (2^10 - 1) / (2 - 1)
    # Test case 4
    assert solution(1, -2, 10) == -341  # Alternating series
    # Test case 5
    assert solution(1, 0.5, 10) == 1.998046875  # Fractional ratio