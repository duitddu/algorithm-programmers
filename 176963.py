# https://school.programmers.co.kr/learn/courses/30/lessons/176963
# 추억 점수

def solution(name, yearning, photo):
    score_dict = dict(zip(name, yearning))
    return sum_scores(score_dict, photo)


def sum_scores(score_dict, photos):
    scores = []
    for photo in photos:
        scores.append(sum_score(score_dict, photo))

    return scores


def sum_score(score_dict, photos):
    score = 0
    for photo in photos:
        if photo in score_dict:
            score += score_dict[photo]

    return score

# def solution(name, yearning, photo):
#    score_dict = dict(zip(name,yearning))
#    return [sum(map(lambda x: score_dict[x] if x in score_dict else 0,p)) for p in photo]