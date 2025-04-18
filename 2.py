#!/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    sys.exit(1)

file = sys.argv[1]
word = sys.argv[2]

try:
    with open(file, 'r') as f:
        for line in f:
            if word in line:
                print(line.strip())
except FileNotFoundError:
    print(f"Файл '{f}' не найден")