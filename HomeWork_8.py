from datetime import datetime, timedelta
from collections import defaultdict
from pprint import pprint


def get_next_week_start(d: datetime):
    diff_days = 7 - d.weekday()
    return d + timedelta(days=diff_days)


def prepare_birthday(text: str):
    bd = datetime.strptime(text, "%d, %m, %Y")
    current_year = datetime.now().year
    try:
        bd = bd.replace(year=current_year)
    except ValueError:
        bd = bd.replace(year=current_year, day=28, month=2)
        if not datetime(current_year, 2, 29).date() <= bd <= datetime(
                current_year, 3, 1).date():
            bd = bd.replace(day=1, month=3)
    return bd.date()


def get_birthdays_per_week(users):
    birthdays = defaultdict(list)
    today = datetime.now().date()

    next_week_start = get_next_week_start(today)
    start_period = next_week_start - timedelta(2)
    end_period = next_week_start + timedelta(4)

    happy_users = [
        user for user in users
        if start_period <= prepare_birthday(user["birthday"]) <= end_period
    ]
    for user in happy_users:
        current_bd = prepare_birthday(user["birthday"])
        if current_bd.weekday() in (5, 6):
            birthdays["Monday"].append(user["name"])
        else:
            birthdays[current_bd.strftime("%A")].append(user["name"])

    return birthdays


if __name__ == "__main__":

    users = [
        {
            "name": "Andrii",
            "birthday": "23, 03, 1968"
        },
        {
            "name": "Anton",
            "birthday": "24, 03, 1998"
        },
        {
            "name": "Petro",
            "birthday": "19, 03, 1994"
        },
        {
            "name": "Oksana",
            "birthday": "18, 03, 1985"
        },
        {
            "name": "Olya",
            "birthday": "20, 03, 1992"
        },
        {
            "name": "Sergii",
            "birthday": "23, 03, 1996"
        },
        {
            "name": "Oleksandr",
            "birthday": "21, 03, 1990"
        },
        {
            "name": "Kiril",
            "birthday": "18, 03, 1994"
        },
        {
            "name": "Mykola",
            "birthday": "25, 03, 1993"
        },
    ]

    result = get_birthdays_per_week(users)
    pprint(result)