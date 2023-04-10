# https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 달리기 경주

def solution(players, callings):
    ranking_dict = create_raking_dict(players)
    return change_rankings(players, callings, ranking_dict)


def create_raking_dict(players):
    return {player: index for index, player in enumerate(players)}


def change_rankings(players, callings, ranking_dict):
    result = players

    for calling in callings:
        ranking = ranking_dict[calling]

        players[ranking] = players[ranking-1]
        players[ranking-1] = calling

        ranking_dict[calling] = ranking-1
        ranking_dict[players[ranking]] = ranking

    return result

# ["mumu", "kai", "mine", "soe", "poe"]
print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))
