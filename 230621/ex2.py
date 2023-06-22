import pandas as pd
from collections import Counter


a= [0, 1, 1]
b = ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]

def solution(picks, minerals):
    answer = 0
    dia_tool_cnt = picks[0]
    iron_tool_cnt = picks[1]
    stone_tool_cnt = picks[2]
    _mine = list_chunk(minerals, 5)
    _df_mine = pd.DataFrame(_mine, )
    _df_mine['diamond'] = _df_mine.apply(lambda x: Counter(x)['diamond'], axis=1)
    _df_mine['iron'] = _df_mine.apply(lambda x: Counter(x)['iron'], axis=1)
    _df_mine['stone'] = _df_mine.apply(lambda x: Counter(x)['stone'], axis=1)
    _df_mine = _df_mine[['diamond', 'iron', 'stone']]
    print('===========================')
    print(_df_mine)
    print('===========================')
    _df_mine = _df_mine.sort_values(by=['diamond', 'iron', 'stone'], ascending=False)
    print('-----------------')
    print(_df_mine)
    print('-----------------')

    # _df_mine.apply(lambda x : print(x), axis=1)
    for _d in _df_mine.values.tolist():
        if dia_tool_cnt:
            answer += sum(_d)
            dia_tool_cnt -= 1
            continue
        if iron_tool_cnt:
            _d[0] = _d[0] * 5
            answer += sum(_d)
            continue
        if stone_tool_cnt:
            _d[0] = _d[0]* 25
            _d[1] = _d[1]* 5
            answer += sum(_d)
            continue
    
    print(answer)
    return answer

def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

# def get_ex(_data, _picks):

if __name__ == "__main__":
    solution(a,b)