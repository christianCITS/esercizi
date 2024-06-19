import random

def mergeSort(list_input:list[int]) -> list[int] :
    
    if len(list_input)==1:
        return list_input

    mid_point:int=len(list_input)// 2
    left_list:int=mergeSort(list_input=list_input[:mid_point])
    right_list:int=mergeSort(list_input=list_input[mid_point:])
    result:list[int]=merge(left_list,right_list)
    return result

def merge(list1,list2):

    i,j=0,0
    result:list[int]=[None for _ in range(len(list1+list2))]

    for k in range(len(result)):
        if list1[i] > list2[j]:
            result[k]=list2[j]
            j+=1
            if j==len(list2):
                    return result[:k+1] + list1[i:]
            
        else:
            result[k]= list1[i]
            i+=1
            
            if i == len(list1):
                return result[:k+1] + list2[j:]
                   



if __name__== "__main__":

    list_input:list[int]=[random.randint(0,100000) for _ in range(100000)]

    result=mergeSort(list_input=list_input[::-1])


    print(result)