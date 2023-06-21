def solution(players, callings):
    answer = []
    print("----------------------------")
    print(players)
    print("----------------------------")

    player = { string : i for i,string in enumerate(players) }
    print(player)
    for _call in callings:
        _idx = player[_call]
        _lose_nm = players[_idx-1]
        players.pop(_idx)
        players.insert(_idx -1, _call)
        
        player[_call] = player[_call] -1
        player[_lose_nm] = player[_lose_nm] +1
        print('------------------------------------111---------------------------')
        print(player)
        print('------------------------------------111---------------------------')

        print(_idx)
    return players


if __name__ == '__main__':
    players = ["mumu", "soe", "poe", "kai", "mine"]
    callings = ["kai", "kai", "mine", "mine"]
    # result = ["mumu", "kai", "mine", "soe", "poe"]
    solution(players, callings)