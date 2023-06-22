# https://school.programmers.co.kr/learn/courses/30/lessons/150370


import pandas as pd

def solution(name, yearning, photo):
    answer = []

    score_data = dict(zip(name, yearning))

    df_photo = pd.DataFrame(photo)

    df_photo['score'] = df_photo.apply(lambda x: add_score(x, score_data), axis=1)
    answer = df_photo['score'].to_list()

    return answer

def add_score(name_list, data_set):
    score = 0
    for _n in name_list:
        if (_n in data_set) is False:
            continue
        score += data_set[_n]
    return score


if __name__ == '__main__':
    name = ["may", "kein", "kain", "radi"]
    yearing = [5, 10, 1, 3]
    photo = [["may", "kein", "kain", "radi"], ["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
    res = solution(name, yearing, photo)
    print(res)