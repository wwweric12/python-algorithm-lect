#퀵정렬
def Qsort(lt,rt): #기준값(pivot)을 정해서 작은값은 왼쪽 큰값을 오른쪽으로 반으로 나눔(전위 순회)
    if lt <rt: 
        pos = lt # lt부터 시작 
        pivot = arr[rt] #기준값
        for i in range(lt,rt):
            if arr[i]<= pivot:
                arr[i],arr[pos] = arr[pos],arr[i]
                pos+=1
        arr[pos] , arr[rt] = arr[rt] , arr[pos]
        Qsort(lt,pos-1)
        Qsort(pos+1,rt)
        
        
        


if  __name__ == "__main__":
    arr=[45,21,23,36,15,67,11,60,20,33]
    print("befor sort : ", end='')
    print(arr)
    Qsort(0,9)
    print()
    print("After sort : ", end='')
    print(arr)