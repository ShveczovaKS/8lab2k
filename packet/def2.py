#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def list():
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+'.format(
        '-' * 30,
        '-' * 20,
        '-' * 14
    )
    print(line)
    print(
        '| {:^30} | {:^20} | {:^14} |'.format(
            "Фамилия, Имя",
            "Номер телефона",
            "Дата рождения",
        )
    )
    print(line)

    # Вывести данные о всех людях.
    for idx, product in enumerate(spisoks, 1):
        print(
            '| {:<30} | {:<20} | {:>14} |'.format(
                product.get('name', ''),
                product.get('tel', ''),
                product.get('date', 0)
            )
        )

    print(line)
