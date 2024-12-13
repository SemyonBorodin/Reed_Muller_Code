from reed_muller_code import ReedMuller
from russian_alphabet import create_russian_dict, symbol_to_message, message_to_symbol


if __name__ == "__main__":
    russian_dict = create_russian_dict()
    rm = ReedMuller(r=2, m=4) 
    message_len = rm.k
    with open("input.txt", "r", encoding="utf-8") as f:
        test_str = f.read().strip()
    
    bin_messages = []
    for symbol in test_str:
        if symbol in russian_dict:
            one_symbol_message = symbol_to_message(symbol, russian_dict, rm.k)
            bin_messages.append(one_symbol_message)
        else:
            bin_messages.append(symbol_to_message(' ', russian_dict, rm.k))
            continue

    encoded_messages = []
    for message in bin_messages:
        encoded = rm.encode(message)
        encoded_messages.append(encoded)

    # Add noise
    noisy_messages = []
    for encoded in encoded_messages:
        noisy = rm.add_noise(encoded)
        noisy_messages.append(noisy)
    
    with open("noisy_messages.txt", "w", encoding="utf-8") as f:
        for noisy in noisy_messages:
            f.write(''.join(map(str, noisy)) + "\n")

    decoded_messages = []
    for noisy in noisy_messages:
        decoded = rm.decode(noisy)
        decoded_messages.append(decoded)

    decoded_str = ""
    for message in decoded_messages:
        decoded_symbol = message_to_symbol(message, russian_dict)
        decoded_str += decoded_symbol

    # print("Декодированная строка:", decoded_str)

    with open("decoded_output.txt", "w", encoding="utf-8") as f:
        f.write(decoded_str)
