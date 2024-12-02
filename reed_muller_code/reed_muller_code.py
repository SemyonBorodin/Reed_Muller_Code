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


def sum_of_powers_of_two(nums, n):
    if not nums:
        return 0
    total_sum = 0
    for num in nums:
        total_sum += 2 ** (n - num - 1)
    return int(total_sum)


def decoder_step_for_fixed_curr_r(message_len, word, curr_mess, r, m):
    num_of_conjunctions = binom(m, r)
    total_sum_for_seq_sums = 0
    len_check_sum = 2 ** (m - r)
    num_check_sums = 2 ** r
    decision_sum = 0
    var_indexes = tuple(range(0, m))
    j, k = 0, 0
    for conjunction in combinations(range(m), r):
        orthogonal_subspace_positions = tuple(x for x in var_indexes if x not in conjunction)
        if k > 0:
            conj_number = int(message_len - num_of_conjunctions + k)
            if decision_sum * 2 >= num_check_sums:
                curr_mess[conj_number] += 1
                curr_mess[conj_number] = curr_mess[conj_number] % 2
            else:
                curr_mess[conj_number] += 0
        k += 1
        decision_sum = 0
        for gamma_size in range(len(orthogonal_subspace_positions) + 1):
            for curr_orthogonal_subspace in combinations(orthogonal_subspace_positions, gamma_size):
                j += 1
                if (j % len_check_sum) == 0:
                    decision_sum += (total_sum_for_seq_sums % 2)
                    total_sum_for_seq_sums = 0
                for t in range(len(conjunction) + 1):
                    for sub_comb in combinations(conjunction, t):
                        check_sum = (sum_of_powers_of_two(sub_comb, m) +
                                     sum_of_powers_of_two(curr_orthogonal_subspace, m))
                        total_sum_for_seq_sums += word[check_sum]
    return curr_mess


rm = ReedMuller(2, 4)

codeword = rm.encode([1]*5 + [1]*6)
print(codeword, 'codeword')
codeword[15] = 0
print(codeword, 'noise added')
print(decoder_step_for_fixed_curr_r(11, codeword,
                                    [0]*11, 2, 4))
