import locale
from datetime import datetime, timedelta

locale.setlocale(locale.LC_TIME, "ru_RU.utf8")

starting_point = datetime.now().strftime("%d %B %Y")
dt = datetime.strptime(starting_point,"%d %B %Y")

def get_date_ago(dt, period, weeks=False):
    '''
    Return date for specified period of time ago

    dt: datetime object for starting point date (today for task)
    period: number of weeks or days ago
    weeks: True means we specified number of weeks. False means days
    '''
    if weeks == True:
        delta_weeks = timedelta(weeks=period)
        weeks_ago_date_dt = dt - delta_weeks
        weeks_ago_date = weeks_ago_date_dt.strftime("%d %B %Y")
        return weeks_ago_date

    else:
        delta_days = timedelta(days=period)
        days_ago_date_dt = dt - delta_days
        days_ago_date = days_ago_date_dt.strftime("%d %B %Y")
        return days_ago_date

if __name__ == "__main__":
    today_date = starting_point
    yesterday_date = get_date_ago(dt, 1)
    month_ago_date = get_date_ago(dt, 4, weeks=True)

    print(today_date)
    print(yesterday_date)
    print(month_ago_date)

    date_string = "01/01/17 12:10:03.234567"
    date_string_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    print(date_string_dt)
    print(type(date_string_dt))
