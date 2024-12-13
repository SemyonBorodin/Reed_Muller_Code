from reed_muller_code import ReedMuller
from russian_alphabet import create_russian_dict, symbol_to_message, message_to_symbol

russian_dict = create_russian_dict()
rm = ReedMuller(2, 4)

def read_noisy_messages(file_path):
    noisy_messages = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            # str from noisy mess to list
            noisy_message = [int(bit) for bit in line.strip()]
            noisy_messages.append(noisy_message)
    return noisy_messages

noisy_messages = read_noisy_messages("noisy_messages.txt")

print(noisy_messages)

decoded_messages =[]

for noisy in noisy_messages:
        decoded = rm.decode(noisy)
        decoded_messages.append(decoded)
decoded_str = ""
for message in decoded_messages:
    decoded_symbol = message_to_symbol(message, russian_dict)
    decoded_str += decoded_symbol

    with open("decoded.txt", "w", encoding="utf-8") as f:
        f.write(decoded_str)
