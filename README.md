# Reed-Muller Code Implementation

This repository contains an implementation of Reed-Muller codes, a class of error-correcting codes that are used in various fields, such as communication systems and data storage. This project focuses on the **encoding** and **decoding** functionalities of Reed-Muller codes. 

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Usage](#usage)
- [Installation](#installation)
- [Project Structure](#project-structure)


## Description

Reed-Muller codes are a family of linear error-correcting codes that can be used for error correction in noisy communication channels. These codes are defined by two parameters:
- `r` (order of the code)
- `m` (number of variables)

The Reed-Muller code of order `r` and length `n = 2^m` is constructed using the generating matrix, which is based on binary polynomials. The class `ReedMuller` in this repository provides methods for:
- Calculating the cardinality `k` of the code
- Generating the generating matrix `G`
- Encoding binary messages of length `k`

The decoder for Reed-Muller codes is currently a placeholder and will be implemented in future updates.

## Features

- **Encoding**: The `encode` method takes a binary message of length `k` and produces a codeword of length `n`.
- **Reed-Muller Generator Matrix**: The `ReedMuller` class computes the generating matrix `G` for the Reed-Muller code based on the order `r` and number of variables `m`.
- **Scalability**: The implementation can handle different values of `r` and `m`, allowing users to work with codes of varying lengths.

## Usage

### Example

```python
from reed_muller_code import ReedMuller

# Initialize Reed-Muller encoder with order 2 and 4 variables
rm_encoder = ReedMuller(r=2, m=4)

# Example message of length k
message = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# Encoding the message
encoded_message = rm_encoder.encode(message)

print(f"Encoded message: {encoded_message}")
