def solution(array1, array2):
    concatenated_array2 = " ".join(array2)
    result = sorted({i for i in array1 if i in concatenated_array2})
    return (result)