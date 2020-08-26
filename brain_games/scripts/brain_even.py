"""Игра 1. Скрипт."""

from brain_games import eveness


def main():
    """Приветствие."""
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".\n')
    eveness.is_even()


if __name__ == '__main__':
    main()
