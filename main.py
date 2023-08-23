from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date


class Accounting:

    def __init__(self, name):
        self.name = name


def main():
    print(date.today())
    accountant = Accounting(name='Anna')
    print('Good morning', accountant.name)
    calculate_salary()
    get_employees()


if __name__ == '__main__':
    main()