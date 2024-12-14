# -*- coding: utf-8 -*-

from reed_muller_code import ReedMuller

def create_russian_dict():
    keys = [' '] + [chr(code) for code in range(ord('а'), ord('я') + 1)]
    return {key: idx for idx, key in enumerate(keys)}

def symbol_to_message(symbol, russian_dict, message_len):
    num = russian_dict[symbol]
    max_bits = len(bin(max(russian_dict.values()))[2:])
    base_message = [int(bit) for bit in bin(num)[2:].zfill(max_bits)]
    return base_message + [0] * (message_len - len(base_message))

def message_to_symbol(message, russian_dict):
    max_bits = len(bin(max(russian_dict.values()))[2:])
    base_message = message[:max_bits]
    value = int(''.join(map(str, base_message)), 2)
    for key, val in russian_dict.items():
        if val == value:
            return key
    return "*"
