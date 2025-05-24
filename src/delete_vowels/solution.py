def solution(string_):

    vowels = "aeiouAEIOU"
    result = ""
    for i in list(string_):
        if i not in vowels:
            result += i
    
    return result