from src.which_are_in.solution import solution

def test_solution():
    # Test case 1
    assert solution(["live", "arp", "strong"],["lively", "alive", "harp", "sharp", "armstrong"]) == ['arp', 'live', 'strong']
    # Test case 2
    assert solution(["tarp", "mice", "bull"],["lively", "alive", "harp", "sharp", "armstrong"]) == []
 

