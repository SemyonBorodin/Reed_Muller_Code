# -*- coding: utf-8 -*-


def create_russian_dict():
    keys = [' '] + [chr(code) for code in range(ord('а'), ord('я') + 1)]
    return {key: idx for idx, key in enumerate(keys)}

def symbol_to_message(symbol, russian_dict, message_len):
    num = russian_dict[symbol]
    return [int(bit) for bit in bin(num)[2:].zfill(message_len)]

russian_dict = create_russian_dict()

def message_to_symbol(message, russian_dict):
    value = int(''.join(map(str, message)), 2)
    for key, val in russian_dict.items():
        if val == value:
            return key
        else:
            return "*"
        
max_bits = len(bin(max(russian_dict.values()))[2:])
print(max_bits)
test_str = 'те ст'
print(test_str)
for el in test_str:
    if el in russian_dict: 
        one_symbol_message = symbol_to_message(el, russian_dict, max_bits)
        print(f"Символ: {el}, Двоичное сообщение: {one_symbol_message}")
    else:
        print(f"Символ '{el}' отсутствует в словаре! *")

