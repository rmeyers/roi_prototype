from datetime import datetime as dt
from datetime import timedelta as td

# This contains the Python functions for the projects dashboard.


def projects_from_db():
    today = dt.today()

    projects_list = [{'name': 'Project 1', 'date': today-td(days=30), 'id': 1},
                     {'name': 'Project 2', 'date': today-td(days=3), 'id': 3},
                     {'name': 'Project 3', 'date': today, 'id': 11}]

    return projects_list
