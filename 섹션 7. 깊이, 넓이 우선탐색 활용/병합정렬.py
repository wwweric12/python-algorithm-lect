#병합 정렬
def Dsort(lt,rt): #두 리스트로 나누고 합치기 (후위순회)
    if lt<rt: 
        mid = (lt+rt)//2
        Dsort(lt,mid) #왼쪽자식
        Dsort(mid+1,rt) #오른쪽자식 
        
        #두가지 영역을 합치는 일  (후위 순회)
        p1=lt
        p2=mid+1
        tmp = []
        while p1 <=mid and p2 <=rt : # p1이 mid를 넘어가거나 p2가 rt를 넘어갈때
            if arr[p1] < arr[p2]:
                tmp.append(arr[p1])
                p1+=1
            else:
                tmp.append(arr[p2])
                p2+=1
        if p1 <= mid : # p2가 rt를 넘어가서 p1이 남아있을때
            tmp= tmp+arr[p1:mid+1]
        if p2 <=rt :
            tmp= tmp+arr[p2:rt+1]
        for i in range(len(tmp)):
            arr[lt+i]=tmp[i] #index가 lt부터 시작이니깐 arr[lt+i]로 해야함 
            
        
        
        
if  __name__ == "__main__":
    arr=[23,11,45,36,15,67,33,21]
    print("befor sort : ", end='')
    print(arr)
    Dsort(0,7)
    print()
    print("After sort : ", end='')
    print(arr)