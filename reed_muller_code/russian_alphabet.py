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

# def create_russian_dict():
#     keys = [' '] + [chr(code) for code in range(ord('а'), ord('я') + 1)]
#     return {key: idx for idx, key in enumerate(keys)}

# def symbol_to_message(symbol, russian_dict, message_len):
#     num = russian_dict[symbol]
#     max_bits = len(bin(max(russian_dict.values()))[2:])
#     base_message = [int(bit) for bit in bin(num)[2:].zfill(max_bits)]
#     return base_message + [0] * (message_len - len(base_message))

# def message_to_symbol(message, russian_dict):
#     max_bits = len(bin(max(russian_dict.values()))[2:])
#     base_message = message[:max_bits]
#     value = int(''.join(map(str, base_message)), 2)
#     for key, val in russian_dict.items():
#         if val == value:
#             return key
#     return "*"  # if too many errors and we can not finde appropriate symbol

# # Создаем словарь русского алфавита
# # russian_dict = create_russian_dict()

# # Example
# # message_len = 8 
# # max_bits = len(bin(max(russian_dict.values()))[2:])

# # test_str = 'те ст'
# # print("Исходная строка:", test_str)

# # to bin
# # bin_messages = []
# # for el in test_str:
# #     if el in russian_dict:
# #         one_symbol_message = symbol_to_message(el, russian_dict, message_len)
# #         bin_messages.append(one_symbol_message)
# #         print(f"Символ: {el}, Двоичное представление: {one_symbol_message}")
# #     else:
# #         print("*")

# # to from dumb binary to Russian
# # decoded_str = ""
# # for message in bin_messages:
# #     decoded_symbol = message_to_symbol(message, russian_dict)
# #     decoded_str += decoded_symbol

# # print(decoded_str)
