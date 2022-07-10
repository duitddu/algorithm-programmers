# https://school.programmers.co.kr/learn/courses/30/lessons/77484?language=python3

UNKNOWN = 0


def solution(lottos, win_nums):
    match_count = 0
    unknown_count = 0

    lottos_set = set(lottos)

    for win_num in win_nums:
        if win_num in lottos_set:
            match_count += 1

    for lotto in lottos:
        if lotto == UNKNOWN:
            unknown_count += 1

    maximum_count = match_count + unknown_count
    minimum_count = match_count
    return [match_count_to_win(maximum_count), match_count_to_win(minimum_count)]


def match_count_to_win(count):
    if count == 6:
        return 1
    elif count == 5:
        return 2
    elif count == 4:
        return 3
    elif count == 3:
        return 4
    elif count == 2:
        return 5
    else:
        return 6
