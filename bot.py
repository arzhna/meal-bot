#!/usr/bin/python
# -*- coding: utf-8 -*-
from mealbot import MealBot
import sys


# Entry Point
if __name__ == '__main__':
    mealbot = MealBot(sys.argv[1] if len(sys.argv) > 1 else None)
    print(mealbot.post())
