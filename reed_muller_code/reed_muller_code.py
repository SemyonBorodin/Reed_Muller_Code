from scipy.special import binom
from itertools import combinations
from random import sample, randint


class ReedMuller:

    def __init__(self, r, m):
        self.r = r  # order
        self.m = m  # num vars
        self.n = 2 ** m  # code word length
        self.k = self._calculate_k()  # cardinality
        self.G = self._generating_matrix()  # generating matrix
        self.t = int(2 ** (self.m - self.r) - 1 / 2)  # correction capability

    # self.codewords = self._generate_codewords() # list of all code words

    def _calculate_k(self):
        k = 0
        for i in range(self.r + 1):
            k += binom(self.m, i)
        return int(k)

    def _generating_matrix(self):
        generating_matrix_columns = []
        for x in range(self.n):
            column = []
            vector_x = []
            for shift in range(self.m):
                bit = (x >> shift) & 1
                vector_x.append(bit)
            for j in range(self.r + 1):
                if j == 0:
                    column.append(1)
                else:
                    for poly_like_indices in combinations(range(self.m), j):
                        val = 1
                        for i in poly_like_indices:
                            val *= vector_x[self.m - i - 1]
                        column.append(val)
            generating_matrix_columns.append(column)
        return generating_matrix_columns

    def get_generating_matrix(self):
        if self.G is None:
            self.G = self._generating_matrix()
        return self.G

    def encode(self, msg):
        if len(message) != self.k:
            raise ValueError("Data length must be equal to k")
        codeword = []
        component = 0
        # scalar product
        for col_num in range(self.n):
            for x, y in zip(msg, self.G[col_num]):
                component += x * y
            codeword.append(component % 2)
            component = 0
        return codeword

    def add_noise(self, codeword):
        return generate_apply_bin_noise(codeword, self.t)

    def decode(self, received):
        pass


def generate_apply_bin_noise(codeword, correction_capability):
    codeword = codeword.copy()
    err_pos = sample(range(len(codeword)), randint(0, correction_capability))  # error positions
    if not err_pos:
        return 'there is to errors'
    for pos in err_pos:
        codeword[pos] ^= 1
    return codeword


rm_code = ReedMuller(2, 4)
message = [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
encoded_message = rm_code.encode(message)
noisy_codeword = rm_code.add_noise(encoded_message)
print(encoded_message, 'encoded_message a.k.a codeword')
print(noisy_codeword, 'noisy_codeword')
print(rm_code.t, 'correction capability of the RM(2,4)')
