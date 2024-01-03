t=int(input("몇번할래??")) 
for i in range(t):
    n,s,e,k=map(int, input("N개의 숫자로 이루어진 숫자열이 주어지면 해당 숫자열중에서 s번째부터 e번째 까지의 수를 오름 차순 정렬했을 때 k번째로 나타나는 숫자를 출력하려고한다 자연수의 개수 ,s번째수 ,e번째수,k 순으로 입력하세요  ").split(' '))
    # lst =input(str(n)+"개의 숫자열을 입력해").split(" ")
    # for i in range(s-1,e):
    #     answer.append(int(lst[i]))    
    answer= list(map(int,input().split())) #리스트에 map 으로 int형으로 추가 
    answer= sorted(answer[s-1:e])
    
    print("#%d %d" %(i+1,answer[k-1]))
    



