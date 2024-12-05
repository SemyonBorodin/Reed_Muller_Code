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
        self.curr_mess = [0] * self.k

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
        if len(msg) != self.k:
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
        curr_mess = [0] * self.k
        for i in range(self.r, -1, -1):
            list_of_index = decoder_step_for_fixed_curr_r(
                self.k,
                received,
                curr_mess,
                i,
                self.r,
                self.m, [])
            print(len(list_of_index), len(list_of_index)/16, list_of_index)
            num_of_conjunctions = int(sum([int(binom(self.m, b)) for b in range(i, self.r + 1, 1)]))
            cur_num_conj = int(binom(self.m, i))
            len_check_sum = 2 ** (self.m - i)
            num_check_sums = 2 ** i
            one_sum = 0
            for t in range(cur_num_conj):
                for d in range(len_check_sum):
                    temp_sum = sum([received[int(list_of_index[w])]
                                   for w in range(0 + d*num_check_sums + t * int(2 ** self.m),
                                   num_check_sums + d*num_check_sums + t * int(2 ** self.m), 1)])
                    print([received[int(list_of_index[w])] for w in range(0 + d*num_check_sums + t * int(2 ** self.m),
                                   num_check_sums + d*num_check_sums + t * int(2 ** self.m), 1)])
                    # print(t, 't'*10)
                    one_sum += temp_sum % 2
                print(one_sum)
                if one_sum * 2 > len_check_sum:
                    curr_mess[self.k - num_of_conjunctions + t] = 1
                    one_sum = 0
                else:
                    curr_mess[self.k - num_of_conjunctions + t] = 0
                    one_sum = 0
                print(curr_mess, 'curr')
        return curr_mess


def generate_apply_bin_noise(codeword, correction_capability):
    codeword = codeword.copy()
    err_pos = sample(range(len(codeword)), randint(0, correction_capability))  # error positions
    if not err_pos:
        return 'there is to errors'
    for pos in err_pos:
        codeword[pos] ^= 1
    return codeword


def sum_of_powers_of_two(nums, n):
    if not nums:
        return 0
    total_sum = 0
    for num in nums:
        total_sum += 2 ** (n - num - 1)
    return int(total_sum)


def decoder_step_for_fixed_curr_r(
        message_len, word,
        curr_mess, r,
        actual_r, m,
        list_of_index):
    one_sum = 0
    var_indexes = tuple(range(0, m))
    j, k = 0, 0
    for conjunction in combinations(range(m), r):
        orthogonal_subspace_positions = tuple(x for x in var_indexes if x not in conjunction)
        k += 1
        # num_of_conjunctions = int(sum([int(binom(m, k)) for k in range(r, actual_r + 1, 1)]))
        for gamma_size in range(len(orthogonal_subspace_positions) + 1):
            for curr_orthogonal_subspace in combinations(orthogonal_subspace_positions, gamma_size):
                for t in range(len(conjunction) + 1):
                    for sub_comb in combinations(conjunction, t):
                        word_index = (sum_of_powers_of_two(sub_comb, m) +
                                      sum_of_powers_of_two(curr_orthogonal_subspace, m))
                        list_of_index.append(word_index)
                        one_sum += word[word_index]
    return list_of_index


rm = ReedMuller(2, 4)
# не корректно работает для малых r
code_word = rm.encode([0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1])
print(code_word)
print(rm.decode(code_word))
print(code_word)
