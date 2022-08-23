import datetime

from const import current_year, dct_fist, dct_last


def get_birthdays_per_week(users):
    week = {
        '1': 'Monday',
        '2': 'Tuesday',
        '3': 'Wednesday',
        '4': 'Thursday',
        '5': 'Friday',
        '6': 'Monday',
        '7': 'Monday',
    }

    congratulations_current_week = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }
    congratulations_next_week = {
        'Monday': '',
        'Tuesday': '',
        'Wednesday': '',
        'Thursday': '',
        'Friday': '',
    }

    today = str(datetime.datetime.isoweekday(datetime.datetime.now()))
    first_current_week = dct_fist[today].date()
    last_current_week = dct_last[today].date()
    first_next_week = last_current_week + datetime.timedelta(days=1)
    last_next_week = first_next_week + datetime.timedelta(days=6)

    for i in users:
        if i['birthday'].year < current_year:
            i['birthday'] = datetime.date(year=current_year, month=i['birthday'].month, day=i['birthday'].day)
            if i['birthday'].month in (first_current_week.month, last_next_week.month):
                if first_current_week <= i['birthday'] <= last_current_week:
                    congratulations_current_week[week[str(datetime.date.isoweekday(i['birthday']))]] += i['name'] + ', '
                elif first_next_week <= i['birthday'] <= last_next_week:
                    congratulations_next_week[week[str(datetime.date.isoweekday(i['birthday']))]] += i['name'] + ', '

    for key, value in congratulations_current_week.items():
        if value != '':
            value = value[:-2]
            congratulations_current_week[key] = value
            print(key + ':', value)
    print('next week')
    for key, value in congratulations_next_week.items():
        if value != '':
            value = value[:-2]
            congratulations_next_week[key] = value
            print(key + ':', value)


get_birthdays_per_week([
    {'name': 'Anna', 'birthday': datetime.date(year=2000, month=8, day=21)},
    {'name': 'Artem', 'birthday': datetime.date(year=2000, month=8, day=25)},
    {'name': 'Dima', 'birthday': datetime.date(year=2000, month=8, day=27)},
    {'name': 'Stepan', 'birthday': datetime.date(year=2000, month=9, day=2)},
    {'name': 'Grisha', 'birthday': datetime.date(year=2000, month=9, day=2)}
])
