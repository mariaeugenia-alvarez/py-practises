from src.multiples_3_5.solution import solution

def test_solution():
    # Test case 1
    assert solution(4) == 3  
    # Test case 2
    assert solution(6) == 8
    # Test case 3
    assert solution(-1) == 0  
    # Test case 4
    assert solution(0) == 0
