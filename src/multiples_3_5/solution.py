def solution(number):
    a=0
    if number >0:
       for i in range(number):
           if (i%5==0) or (i%3==0):
            a=i+a
    return (a)