# Write a function that receives as parameter a matrix and will return the matrix
# obtained by replacing all the elements under the main diagonal with 0 (zero).


def replace_under(matrix, n, m):
    for c in range(0, m):
        for r in range(c, n):
            if c != r:
                matrix[r][c] = 0
    return matrix


m_rows = int(input("Give number of rows: "))
m_columns = int(input("Give number of columns: "))

in_matrix = []
print("Give matrix: ")

for i in range(m_rows):
    row = []
    for j in range(m_columns):
        row.append(int(input()))
    in_matrix.append(row)

m = replace_under(in_matrix, m_rows, m_columns)
for i in range(m_rows):
    row = []
    for j in range(m_columns):
        row.append(m[i][j])
    print(row)


