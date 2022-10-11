#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import random

with open("./hyakuinin.txt", encoding="utf-8") as f:
    wakas = [s.strip() for s in f.readlines()]

print(wakas[random.randrange(len(wakas))])
