def checkio(numbers_array):
    numbers_array = list(numbers_array)
    for x in range(len(numbers_array)):
        for y in range(len(numbers_array)):
            if abs(numbers_array[x]) < abs(numbers_array[y]):
                numbers_array[x],numbers_array[y] = numbers_array[y],numbers_array[x]
    print(numbers_array)
    return numbers_array
    

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [-5, 10, 15, -20], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"
