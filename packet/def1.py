#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def add():
    # Запросить данные .
    name = input("Фамилия, Имя ")
    tel = input("Номер телефона ")
    date = input("Дата рождения ")

    # Создать словарь.
    spisok = {
        'name': name,
        'tel': tel,
        'date': date}

    # Добавить словарь в список.
    spisoks.append(spisok)
    # Отсортировать список в случае необходимости.
    if len(spisok) > 1:
        spisoks.sort(key=lambda item: item.get('tel', ''))
