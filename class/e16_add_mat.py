"""
(A little introduction to functions)
I'd like you to write a function that accepts two lists-of-lists of numbers and returns one list-of-lists with each of
the corresponding numbers in the two given lists-of-lists added together.

It should work something like this:

>> matrix1 = [[1, -2], [-3, 4]]
>> matrix2 = [[2, -1], [0, -1]]
>> add(matrix1, matrix2)
[[3, -3], [-3, 3]]
>> matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
>> matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
>> add(matrix1, matrix2)
[[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

Try to solve this exercise without using any third-party libraries (without using pandas, for example).

"""
def add(matrix1, matrix2):
    result = [[] for _ in range(len(matrix1))]
    k, j = 0, 0
    while k < len(matrix1):
        while j < len(matrix1[k]):
            result[k].append(matrix1[k][j] + matrix2[k][j])
            j +=1
        j = 0
        k += 1
    return result



