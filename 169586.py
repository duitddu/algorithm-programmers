# https://school.programmers.co.kr/learn/courses/30/lessons/160586
# 대충 만든 자판

def solution(keymap, targets):
    key_dict = get_key_move_dict(keymap)
    return get_keymap_result(key_dict, targets)


def get_key_move_dict(keymap):
    key_dict: dict[str, int] = {}

    for keys in keymap:
        for i, key in enumerate(keys):
            key_dict[key] = min(i + 1, key_dict[key]) if key in key_dict else i + 1

    return key_dict


def get_keymap_result(key_dict, targets):
    return [get_key_result(key_dict, target) for target in targets]


def get_key_result(key_dict, target):
    result = 0
    for target_key in target:
        if target_key not in key_dict:
            return -1

        result += key_dict[target_key]

    return result


# [9, 4]
print(solution(["ABACD", "BCEFD"], ["ABCD", "AABB"]))

# [-1]
print(solution(["AA"], ["B"]))

# [9, 4]
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"]))
