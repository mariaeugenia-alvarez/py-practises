from src.delete_vowels.solution import solution

def test_solution():
    # Test case 1
    assert solution("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
        # Test case 2
    assert solution("No offense but,\nYour writing is among the worst I've ever read") == "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"
    # Test case 3
    assert solution("What are you, a communist?") == "Wht r y,  cmmnst?"
   