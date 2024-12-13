# Reed-Muller Code Implementation

This repository contains an implementation of Reed-Muller codes, a class of error-correcting codes that are used in various fields, such as communication systems and data storage. This project focuses on the **encoding** and **decoding** functionalities of Reed-Muller codes. 

## Table of Contents

- [Description](#description)
- [Usage](#usage)
- [Example](#example)
- [Installation](#installation)

## Description

Reed-Muller codes are a family of linear error-correcting codes that can be used for error correction in noisy communication channels. These codes are defined by two parameters:
- `r` (order of the code)
- `m` (number of variables)

The Reed-Muller code of order `r` and length `n = 2^m` is constructed using the generating matrix, which is based on binary polynomials. The class `ReedMuller` in this repository provides methods for:
- Calculating the cardinality `k` of the code
- Generating the generating matrix `G`
- Encoding binary messages of length `k`
- Decoding of noisy messages using a checksum-based algorithm.

## Usage

0. **RM-codes:**

```python
from reed_muller_code import ReedMuller

# Initialize the Reed-Muller code with desired parameters
rm_code = ReedMuller(r=2, m=4)

# Example message to encode
message = [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]

# Encode the message
encoded_message = rm_code.encode(message)

# Add noise (optional, for testing decoding)
noisy_message = add_noise(encoded_message)

# Decode the noisy message
decoded_message = rm_code.decode(noisy_message)

print(f"Original Message: {message}")
print(f"Encoded Message: {encoded_message}")
print(f"Noisy Message: {noisy_message}")
print(f"Decoded Message: {decoded_message}")
```
   
1. **Creating dictionary and initializing `ReedMuller`:**

```python
russian_dict = create_russian_dict()
rm = ReedMuller(r=2, m=4)
message_len = rm.k
```

2. **Reading string from input.txt:**

```python
with open('input.txt', 'r', encoding='utf-8') as f:
    input_str = f.read()
```

3. **Transform character strings to binary representation and encode them:**

```python
with open('input.txt', 'r', encoding='utf-8') as f:
    input_str = f.read()
```

4. **Encode and add noise:**

```python
bin_messages = []
for symbol in input_str:
    if symbol in russian_dict:
        one_symbol_message = symbol_to_message(symbol, russian_dict, rm.k)
        bin_messages.append(one_symbol_message)
```

5. **Decode noisy messages in a string notation of zeros and ones and save the result to a file:**

```python
bin_messages = []
for symbol in input_str:
    if symbol in russian_dict:
        one_symbol_message = symbol_to_message(symbol, russian_dict, rm.k)
        bin_messages.append(one_symbol_message)
```


### Example
5. "Decode noisy messages:"

```python
bin_messages = [
    "0000111100001000",
    "0011011100111100",
    "0110011001100110",
    "0101010110100001",
    "0000000000000000",
    "0011111000111100",
    "0110011001000110",
    "0101010111101010",
    "0000000000000000",
    "0000000111111111",
    "0110100101100110",
    "0000000000000000",
    "0011100000110011",
    "0110011001100110",
    "0011001100111100",
    "0101010101011110",
    "0110011001100110",
    "0011001100111100",
    "0110100110010001",
    "0000000000000000",
    "1101010101011010",
    "0000111100000000",
    "0011001100111100",
    "0000111000000000",
    "0101010110101101",
    "0000000000000000",
    "0101010101011010",
    "0000000000000000",
    "0110100101100110",
    "0011001100110011",
    "0110100101101001",
    "0110011001101110",
    "0100000000000000",
    "0101010101011010",
    "0110100101101001",
    "0011001111001100",
    "0101010110100100",
    "0000000011110001",
    "0000111100000000",
    "0000000000000000",
    "0011110000110011",
    "0000000000001111",
    "0000101111111111",
    "0000110100000000",
    "0110110101101001",
    "1000000000001111",
    "0000000010000000",
    "0101010110101011",
    "0110011001100100",
    "0011110000111100",
    "0000000000000000",
    "0101010100011010",
    "0000000010000000",
    "0110101101100110",
    "0011001100110011",
    "0110100101100110",
    "0100100101101001",
    "0011110011001100",
    "0000000000000001",
    "0001111100000000",
    "0000000000000100",
    "0011001111001100",
    "0110011001100110",
    "1110011010011001",
    "0000000000001111",
    "0011110000111100",
    "0000001000000000",
    "0000000000000000",
    "0000000100000000"]
decoded_mes = "идет лес по медведю видит в огне внутри машина сел в огонь и уехал"
```
## Installation

To install the necessary dependencies, you need this packages:

```python
from scipy.special import binom
from itertools import combinations
from random import sample, randint
```
The project requires Python 3.x and the scipy library for computing binomial coefficients used in the decoding algorithm;
combinations from itertools; 
sample, randint from random.



