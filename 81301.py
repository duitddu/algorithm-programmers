# https://school.programmers.co.kr/learn/courses/30/lessons/81301

NUM_LIST = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
]

NUM_DICT = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def solution(s):
    answer = 0

    while len(s) > 0:
        answer *= 10

        if s[0].isdigit():
            answer += int(s[0])
            s = s[1:]
        else:
            num = find_start_number(s)
            answer += NUM_DICT[num]
            s = s.replace(num, "", 1)

    return answer


def find_start_number(s):
    for num in NUM_LIST:
        if s.startswith(num):
            return num
    return ""