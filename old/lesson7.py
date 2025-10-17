def flatten_2d_list(matrix):
    flat_list = []
    for sublist in matrix:
        for item in sublist:
            flat_list.append(item)
            return flat_list

print(flatten_2d_list([[1,2],[3,4]]))


