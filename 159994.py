# https://school.programmers.co.kr/learn/courses/30/lessons/159994
# 카드 뭉치

def solution(cards1, cards2, goal):
    return "Yes" if create_sentence(cards1, cards2, goal) else "No"


def create_sentence(cards1: [str], cards2: [str], goal: [str]) -> bool:
    for goal_word in goal:
        if len(cards1) > 0 and cards1[0] == goal_word:
            del cards1[0]
        elif len(cards2) > 0 and cards2[0] == goal_word:
            del cards2[0]
        else:
            return False
    return True
