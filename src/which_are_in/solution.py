def solution(array1, array2):
    final_list= []
    for i in array1:
        for j in array2:
            if (i in j) and (i not in final_list):
                final_list.append(i)
                
    sort_list=sorted(final_list)
    return (sort_list)
