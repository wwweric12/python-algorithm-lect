from heapq import heappush, heappop

def solution(k, n, reqs):
    def cal_wait_time(waitings, n):  # 유형 별 waiting_list에 n명의 상담 원이 있을 때 대기 시간 계산
        total_time = 0
        counsel_list = []
        for _ in range(n):
            heappush(counsel_list, 0)
        for start, duration in waitings:
            prev_end = heappop(counsel_list)  # 자리가 생기는 시간
            if start > prev_end:  # 바로 상담 가능
                heappush(counsel_list, start + duration)
            else:
                wait_time = prev_end - start
                total_time += wait_time
                heappush(counsel_list, prev_end + duration)
        return total_time

    result = 1e9

    # 유형별 요청 분리
    waiting_list = [[] for _ in range(k)]
    for req in reqs:
        waiting_list[req[2] - 1].append([req[0], req[1]])

    # DFS를 통한 멘토 배치 조합 구하기
    mentos = []
    ch = [1] * k  # 각 유형당 최소 1명씩 배치

    def dfs(L, idx):
        if L == n - k:
            mentos.append(ch.copy())
            return
        for i in range(idx, k):
            ch[i] += 1
            dfs(L + 1, i)
            ch[i] -= 1

    dfs(0, 0)

    for case in mentos:
        time = 0
        for i in range(k):
            time += cal_wait_time(waiting_list[i], case[i])
        result = min(result, time)

    return result
