def solution(a, r, n):
    if isValidArgs(a, r, n):
            expected = calculate(a, r, n)    
    return(expected)

def calculate(a, r, n):
    isBaseCase = r==1
    if isBaseCase:
        expected=a*n
    else:
        expected=calculateComplexCase(a, r, n)
    return expected

def isValidArgs(a, r, n):
    return (1<= a <=10) and (-10<= r <=10) and (2<= n <=15)

def calculateComplexCase(a, r, n):
    return a*(((r**n)-1)/(r-1))