from src.sort_string.solution import solution

def test_solution():
    # Test case 1
    assert solution("is2 Thi1s T4est 3a") == "Thi1s is2 3a T4est" 
    # Test case 2
    assert solution("4of Fo1r pe6ople g3ood th5e the2") == "Fo1r the2 g3ood 4of th5e pe6ople"
    # Test case 3
    assert solution("") == "" 

