#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运行:      python3 helloworld.py
输入测试:  python3 helloworld.py < input.txt
管道测试:  echo "3 4" | python3 helloworld.py
"""

import sys


def solve(data: str) -> str:-
    tokens = data.split()              
    lines = data.strip().splitlines()  

    return str(result)


def main() -> None:
    data = sys.stdin.read()
    out = solve(data)
    if out:
        print(out)


if __name__ == "__main__":
    main()
