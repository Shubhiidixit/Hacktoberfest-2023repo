import sys

def matrix_chain_multiplication(dims):
    n = len(dims) - 1  # Number of matrices
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for chain_length in range(2, n + 1):
        for i in range(1, n - chain_length + 2):
            j = i + chain_length - 1
            m[i][j] = sys.maxsize  # Initialize to a large value

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m[1][n]

def print_optimal_parentheses(s, i, j):
    if i == j:
        print(f'Matrix {i}', end='')
    else:
        print('(', end='')
        print_optimal_parentheses(s, i, s[i][j])
        print_optimal_parentheses(s, s[i][j] + 1, j)
        print(')', end='')

# Example usage
matrix_dimensions = [10, 30, 5, 60]
min_operations = matrix_chain_multiplication(matrix_dimensions)
print(f"Minimum number of multiplications: {min_operations}")

print("Optimal Parentheses for Multiplication:")
print_optimal_parentheses(s, 1, len(matrix_dimensions) - 1)
