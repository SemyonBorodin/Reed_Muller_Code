class ReedMuller:
    def __init__(self, r, m):
        self.r = r  # order
        self.m = m  # num vars
        self.n = 2 ** m  # code word length
        self.k = self._calculate_k()  # cardinality
        self.G = self._generating_matrix()  # generating matrix

    # self.codewords = self._generate_codewords() # list of all code words

    def _calculate_k(self):
        import scipy.special
        k = 0
        for i in range(self.r + 1):
            k += scipy.special.binom(self.m, i)
        return int(k)

    def _generating_matrix(self):
        from itertools import combinations

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

    def encode(self, message):
        if len(message) != self.k:
            raise ValueError("Data length must be equal to k")
        codeword = []
        component = 0
        # scalar product
        for col_num in range(self.n):
            for x, y in zip(message, self.G[col_num]):
                component += x * y
            codeword.append(component % 2)
            component = 0
        return codeword

    def decode(self, received):
        # TO DO
        pass


# print(ReedMuller._generating_matrix(ReedMuller(2, 4)))
# ReedMuller.encode(ReedMuller(2, 4), [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
