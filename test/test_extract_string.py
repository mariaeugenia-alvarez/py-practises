from src.extract_string.solution import solution

def test_solution():
    # Test case 1
    assert solution(["Ryan", "Kieran", "Mark"]) == ["Ryan", "Mark"]
    # Test case 2
    assert solution(["Ryan", "Jimmy", "abc", "d", "Cool Man"]) == ["Ryan"]
    # Test case 3
    assert solution(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == ["Jimm", "Cari", "aret"]