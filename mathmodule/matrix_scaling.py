def multiply(left_matrix, right_matrix):
    """
    Matrix multiplication, matrices are given by either two lists or a list and a dictionary

    :param left_matrix: matrix, list or dict, but if dict than :param right_matrix should be list
    :param right_matrix: matrix, list or dict, but if dict than :param left_matrix should be list
    :return: multiplied by each other matrices :type list
    """
    if type(left_matrix) == list and type(right_matrix) == list:
        zip_right = list(transpose_matrix(right_matrix))
        return [[sum(elem_a * elem_b for elem_a, elem_b in zip(row_a, row_b))
                 for row_b in zip_right] for row_a in left_matrix]

    if type(left_matrix) == dict and type(right_matrix) == list:
        zip_right = list(transpose_matrix(right_matrix))
        return [[sum(elem_a * elem_b for elem_a, elem_b in zip(item.values(), row_b))
                 for row_b in zip_right] for key, item in left_matrix.items()]

    if type(right_matrix) == dict and type(left_matrix) == list:
        zip_left = list(transpose_matrix(left_matrix))
        return [[sum(elem_a * elem_b for elem_a, elem_b in zip(item.values(), row_b))
                 for row_b in zip_left] for key, item in right_matrix.items()]


def transpose_matrix(matrix):
    """
    Transposes the matrix
    :param matrix: Matrix :type list,dict
    :return: Transposed matrix :type list,dict
    """

    if type(matrix) == dict:
        transposed_matrix = {}
        for key, item in matrix.items():
            transposed_matrix[key] = {item_key: None for item_key in item.keys()}

        for new_key, new_item in transposed_matrix.items():
            value_list = []
            for old_key, old_item in matrix.items():
                value_list.append(old_item.get(new_key, 0))

            transposed_matrix[new_key] = dict(zip(new_item.keys(), value_list))

        return transposed_matrix

    for row in matrix:
        if len(row) != len(matrix):
            raise ValueError('Matrix is not square')

    transposed_matrix = []
    for iter in range(len(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[iter])

        transposed_matrix.append(new_row)

    return transposed_matrix


if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    matrix_2 = [[2, 3, 5],
                [4, 6, 8],
                [9, 10, 7]]
    matrix_dict = {1: {1: 0, 2: 0, 3: 0},
                   2: {1: 0, 2: 0, 3: 0},
                   3: {1: 7, 2: 0, 3: 9}}
    # print(multiply(matrix, matrix_2))
    # print(multiply(matrix_dict, matrix_2))
    print(multiply(matrix_2, matrix_dict))
    print(transpose_matrix(transpose_matrix(matrix_dict)))






