# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 문자열 나누기

def solution(s):
    answer = 0

    while len(s) > 0:
        divide_index = divide(s)
        answer += 1
        s = s[divide_index+1:]

    return answer


def divide(s):
    x = s[0]
    x_count = 1
    not_x_count = 0

    for i in range(1, len(s)):
        c = s[i]
        if c == x:
            x_count += 1
        else:
            not_x_count += 1

        if x_count == not_x_count:
            return i

    return len(s) - 1

# 3, ba-na-na
# print(solution("banana"))

# 6, ab - ra - ca - da - br - a
# print(solution("abracadabra"))

# 3, aaabbacc - ccab - ba
print(solution("aaabbaccccabba"))