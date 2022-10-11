#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import random

def main():

    with open("./hyakuinin.txt", encoding="utf-8") as f:
        wakas = [s.strip() for s in f.readlines()]
        print("今日の一句" + wakas[random.randrange(len(wakas))])


if __name__ == '__main__':
    main()
