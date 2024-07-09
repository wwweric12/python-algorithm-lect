def solution(today, terms, privacies):
    answer = []
    terms_dict={}  
    today_year,today_month,today_day = map(int,today.split("."))
    for i in range(len(terms)):
        sort, month = terms[i].split()
        terms_dict[sort]=int(month)
    index=1
    for privacy in privacies:
        privacy_date,privacy_sort=privacy.split()
        privacy_year,privacy_month,privacy_day = map(int,privacy_date.split("."))
        privacy_month+=terms_dict[privacy_sort]
        tmp_quote=privacy_month//12 
        privacy_month%=12
        if privacy_month ==0:
            tmp_quote-=1
            privacy_month=12
        privacy_year+=tmp_quote
        
        if privacy_year < today_year: # 년도가 오늘이 더 클때 파기
            answer.append(index)
        elif privacy_year ==  today_year:
            if today_month > privacy_month : #년도가 같은데 월이 더 클때도 파기 
                answer.append(index)
            elif privacy_month ==  today_month and today_day >= privacy_day:
                answer.append(index)

        index+=1
        
        
    return answer