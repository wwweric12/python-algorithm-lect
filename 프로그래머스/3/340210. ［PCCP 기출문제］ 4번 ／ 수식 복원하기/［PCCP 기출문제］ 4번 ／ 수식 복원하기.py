## 2진법~ 9진법
## 결과값을 맞게 채우는데 
## 모르는것은 ? 로 

## 숫자로 바꿔서 10진법이랑 값을 비교해서 
## 원래값과의 차이로 몇진법인지 알아내기 
## 숫자가 나타나면 그진법보다는 위 즉 7이 나오면 최소 8진법이라는 것 
## 만약 8이 나오면 9진법은 확정 



## 완성된 수식으로  진법 계산 
def com_calculator(cal):
    a =  int(cal[0])
    b =  int(cal[2])
    res= 0
    ans = -1
    if cal[1] == "-":
        ans = find_ginbub(a,b,cal[4],"-")
    elif cal[1] == "+":
        ans = find_ginbub(a,b,cal[4],"+")
    return ans

## 계산이 가능한지 
def can_cal(a,b,result,ginbub,susik):
    a=str(a)
    b=str(b)
    min_length =len(a)
    if len(a)> len(b):
        gap = len(a)-len(b)
        b= ("0"*gap)+b
    elif len(a)< len(b):
        gap = len(b)-len(a)
        a= ("0"*gap)+a
        min_length =len(b)
    if susik == "+":
        for i in range(min_length-1,-1,-1):
            if int(a[i])+int(b[i])>=ginbub:
                return False
    else:
        for i in range(min_length-1,-1,-1):
            if int(a[i])-int(b[i])<0:
                return False
    return True

def calculator_value(a,b,ginbub,susik):
    a=str(a)
    b=str(b)
    min_length =len(a)
    if len(a)> len(b):
        gap = len(a)-len(b)
        b= ("0"*gap)+b
    elif len(a)< len(b):
        gap = len(b)-len(a)
        a= ("0"*gap)+a
        min_length =len(b)
        
    ans=""
    if susik == "+":
        nxt_plus=0
        for i in range(min_length-1,-1,-1):     
            tmp_value =int(a[i])+int(b[i])+nxt_plus
            nxt_plus= tmp_value // ginbub
            ans += str(tmp_value%ginbub)
        if nxt_plus:
            ans += str(nxt_plus)
    else:
        nxt_minus=0
        for i in range(min_length-1,-1,-1):
            tmp_value =int(a[i])-int(b[i])+nxt_minus
            nxt_minus=0
            if tmp_value <0 :
                nxt_minus = -1
                tmp_value+=ginbub
            ans += str(tmp_value)
    
    result=ans[::-1]
    for i in range(len(ans)):
        if result[i]== "0":
            if i == len(ans)-1:
                result = "0"
            continue
        else:
            result = result[i::]
            break
        
    
    if result == "":
        result = "0"
    return result
    


## 답 도출
def uncom_calculator(cal,flag,ginbub):
    a =  int(cal[0])
    b =  int(cal[2])
    res="?"
    if ginbub == 9:
        flag = 1 
    
    if flag ==1 :
        if cal[1] == "-":
            res=calculator_value(a,b,ginbub,"-")
            
        elif cal[1] == "+":
            res= calculator_value(a,b,ginbub,"+")
    else:
        if cal[1] == "-":
            tmp = a-b 
            if can_cal(a,b,tmp,ginbub,"-"):
                res= calculator_value(a,b,ginbub,"-")
        elif cal[1] == "+":
            tmp = a+b 
            if can_cal(a,b,tmp,ginbub,"+"):
                res= calculator_value(a,b,ginbub,"+")
    
    return res


## 몇진법인지 확인 
def find_ginbub(a,b,value_unknown,susik):
    possible = []
    for i in range(2, 10):
        res = calculator_value(a, b, i, susik)
        if res == value_unknown:
            possible.append(i)

    if len(possible) == 1:  # 유일하게 하나일 때만
        return possible[0]
    else:
        return -1    
    


## 숫자가 얼마나 나왔는지 몇진법인지 확인 
def cal_ginbub(expression):
    tmp=0
    for st in expression:
        if st.isdigit():
            tmp= max(tmp,int(st))
    
    return tmp+1
    
    
        

def solution(expressions):
    answer = []
    ginbub=0
    complete=[]
    unComplete=[]
    flag =0 
    for expression in expressions:
        ginbub = max(ginbub,cal_ginbub(expression))    
        tmp=list(expression.split())
        if tmp[4] == "X":
            unComplete.append(tmp)
        else:
            complete.append(tmp)
            
    
    for com_exp in complete:
        tmp_ginbub=com_calculator(com_exp)
        if  tmp_ginbub!=-1:
            flag=1
            ginbub=tmp_ginbub
            break
    
    
    for uncom_exp in unComplete:
        res = uncom_calculator(uncom_exp,flag,ginbub)
        uncom_exp[4]=res
        tmp=""
        for i in range (len(uncom_exp)):
            tmp+=uncom_exp[i]
            if i != len(uncom_exp)-1:
                tmp+=" "
        answer.append(tmp)
        
    
    
    return answer