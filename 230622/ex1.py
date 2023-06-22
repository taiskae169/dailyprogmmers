import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

# https://school.programmers.co.kr/learn/courses/30/lessons/150370
# 문제 푸는중

def solution(today, terms, privacies):
    answer = []

    df_terms = pd.DataFrame(terms)
    df_privacies = pd.DataFrame(privacies)

    df_terms[['cate', 'month']] = df_terms[0].str.split(' ', expand=True)
    df_terms = df_terms[['cate', 'month']]

    df_privacies[['dt', 'cate']] = df_privacies[0].str.split(' ', expand=True)
    df_privacies = df_privacies[['cate', 'dt']]
    # df_terms[['cate', 'month']] = '1','2'

    _df_data_set = pd.merge(df_privacies, df_terms, 'left', 'cate')
    _df_data_set['today'] = today
    _df_data_set.apply(lambda x: check_dt(x), axis=1)
    # _df_data_set['is_deleted'] = _df_data_set.apply(lambda x: print(x), axis=1)
    print(_df_data_set)

    return answer

def check_dt(x):
    get_pri_dt = datetime.strptime(x['dt'], '%Y.%m.%d')
    current_dt = datetime.strptime(x['today'], '%Y.%m.%d')
    _ex_dt = int(x['month']) * 28 + (28 - get_pri_dt.day)
    add_year = int(_ex_dt / (12 * 28))
    _ex_dt -= add_year * 12 * 27
    print(_ex_dt)
    add_month = int(_ex_dt/28)
    _ex_dt -= add_month * 28
    add_day = _ex_dt
    # add_day = get_pri_dt.day +  _ex_dt -1
    # add_month = int(add_day /28)
    # add_day = add_day % 28
    # add_year = int(add_month/12)
    # add_month = add_month % 12

    print("*****************************")
    print(add_year)
    print(add_month)
    print(add_day)
    print("*****************************")
    # expire_dt = datetime(year=get_pri_dt.year + add_year, month= get_pri_dt.month + add_month, day=add_day)

    # print(get_pri_dt.year)
    # print(get_pri_dt.month +2)
    # print(get_pri_dt.day)\
    expire_dt = get_pri_dt + relativedelta(days=int(x['month']) * 28)
    # expire_dt = datetime(year=expire_dt.year, month= expire_dt.month, day=get_pri_dt.day)
    # expire_dt = datetime(year=get_pri_dt.year, month= get_pri_dt.month + int(x['month']), day=get_pri_dt.day)
    print('')
    print('get_pri_dt' , get_pri_dt)
    print('expire_dt' ,expire_dt)
    print('current_dt' ,current_dt)
    print('')

    if expire_dt <= current_dt:
        print('파기!')
    # month_diff = diff.years * 12 + diff.months
    return x


if __name__ == '__main__':
    today = "2022.05.19"
    terms = ["A 6", "B 12", "C 3"]
    privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
    result = [1,3]
    res = solution(today, terms, privacies)
    print(res)

    # print('aaaa ddd'.split(' '))