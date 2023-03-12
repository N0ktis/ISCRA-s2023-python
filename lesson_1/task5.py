"""
Copyright 2023 aaaaaaaalesha

В стандартный поток ввода передается текст (латинница) в одну строку.
Далее следует целое число - ключ шифрования.
Выведете результат шифрования строки шифром Цезаря для данной строки и ключа.

>> i am atomic
>> 7

Out: phthavtpj
"""
from string import ascii_lowercase as ALPHABET

shifted_ascii_codes = list(map(
    lambda c: ord(c) - ord(ALPHABET[0]),
    list(input().replace(' ', '')),
))
key = int(input())

print(''.join(
    chr((code + key) % len(ALPHABET) + ord(ALPHABET[0]))
    for code in shifted_ascii_codes
))
