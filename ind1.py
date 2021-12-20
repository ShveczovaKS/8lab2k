#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import module

if __name__ == '__main__':
    A = input("Введите тег - ")
    B = input("Введите строку - ")
    print(module.get_func(A)(B))
