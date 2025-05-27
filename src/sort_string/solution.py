def solution(sentence):
    list=sentence.split()
    dict={}  
    
    for i in list:
        look_digit(dict, i)
    
    sort_dict= sorted(dict.keys()) #Ordeno las claves del diccionario
    sort_list= [] # For para incluir los valores del dict en lista
    for key in sort_dict:
        sort_list.append(dict[key])    

    sort_sent= " ".join(sort_list) #pasarlo a string
    return (sort_sent)

def look_digit(dict, i):
    for j in i:
        insert_dictionary(dict, i, j)

def insert_dictionary(dict, i, j):
    if j.isdigit():
        dict[int(j)]=i