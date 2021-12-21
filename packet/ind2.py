#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from packet import sys, def1, def2, def3, def4

if __name__ == '__main__':

    # Список
    spisoks = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>>>>>", ).lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            def1.add()

        elif command == 'list':
            def2.list()

        elif command.startswith('select '):
            def3.select()

        elif command == 'help':
            def4.help()
        else:
            print("Неизвестная команда {command}", file=sys.stderr)
