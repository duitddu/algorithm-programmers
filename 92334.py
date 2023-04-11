# https://school.programmers.co.kr/learn/courses/30/lessons/92334
# 신고 결과 받기

def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]
    report_set = set(report)
    reported_count_dict = {user: 0 for _, user in enumerate(id_list)}

    for r in report_set:
        _, reported = r.split(" ")
        reported_count_dict[reported] += 1

    for r in report_set:
        reporter, reported = r.split(" ")
        if reported_count_dict[reported] >= k:
            answer[id_list.index(reporter)] += 1

    return answer

# [2,1,1,0]
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
