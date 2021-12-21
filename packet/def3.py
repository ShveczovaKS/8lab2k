#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def select():
    parts = command.split(' ', maxsplit=2)
    sel = (parts[1])

    count = 0
    for spisok in spisoks:
        if spisok.get('name') == sel:
            count = "Дата рождения"
            print(
                '{:>4}: {}'.format(count, spisok.get('date', ''))
            )
            print('Номер телефона', spisok.get('tel', ''))
            print('Фамилия Имя', spisok.get('name', ''))

    # Если счетчик равен 0, то рейсы не найдены.
    if count == 0:
        print("Люди не найден.")
