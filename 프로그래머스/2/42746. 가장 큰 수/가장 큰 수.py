
def solution(numbers):
    answer = ''
    str_numbers=[]    
    for number in numbers:
        tmp = str(number)*3
        str_numbers.append(tmp)
    str_numbers.sort(reverse=True)
    
    for str_num in str_numbers:
        k = len(str_num)//3
        answer+=str(int(str_num[:k]))
    
    
    if answer[0] == "0":
        answer = str(int(answer))

            
        
    
    return answer