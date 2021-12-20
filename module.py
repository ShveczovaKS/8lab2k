#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_func(tag):
    def func(s):
        group = tag, s

        return group

    return func


