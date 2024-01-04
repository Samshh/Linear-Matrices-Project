import numpy as np

#part 1
def generate_matrix_a():
    return np.array([5, 1, 2, 1, 3, 7, 2, 7, 8]).reshape(3, 3)

def generate_matrix_b():
    return np.array([-1, 2, -4, 5]).reshape(4, 1)

def generate_matrix_c():
    return np.zeros((3, 2))

def generate_matrix_d():
    return np.array([2, 1, 3, 6, 7])

def add_matrices(matrix_1, matrix_2):
    try:
        result = np.add(matrix_1, matrix_2)
        return result
    except ValueError:
        print(f"\nNot Possible")

def subtract_matrices(matrix_1, matrix_2):
    try:
        result = np.subtract(matrix_1, matrix_2)
        return result
    except ValueError:
        print("\nNot Possible")

def multiply_matrices(matrix_1, matrix_2):
    try:
        result = np.matmul(matrix_1, matrix_2)
        return result
    except ValueError:
        print("\nNot Possible")

#part 2
def add_AB():
    matrix_a = np.array([2, 1, 3, 3, -2, 1, -1, 0, 1]).reshape(3, 3)
    matrix_b = np.array([1, -2, 2, 1, 4, -2]).reshape(3, 2)
    try:
        result = add_matrices(matrix_a, matrix_b)
    except ValueError:
        return None
    if result is not None:
        print(f"\n{result}")

def mul_AB(): # needs rework it should be -12?
    matrix_a = np.array([2, 1, 3]).reshape(1, 3)
    matrix_b = np.array([-2, 1, 3]).reshape(3, 1)
    try:
        result = multiply_matrices(matrix_a, matrix_b)
    except ValueError:
        return None
    if result is not None:
        print(f"\n{result}")

def add_FH():
    matrix_f = np.array([2, -1, 3, 0, -5, 2]).reshape(3, 2)
    matrix_h = np.array([1, 6, -1, -2, 0, -3]).reshape(3, 2)
    try:
        result = add_matrices(matrix_f, matrix_h)
    except ValueError:
        return None
    if result is not None:
        print(f"\n{result}")

def sub_CA():
    matrix_c = np.array([3, -1, -2, 2]).reshape(2, 2)
    matrix_a = np.array([2, 0, 1, 4]).reshape(2, 2)
    try:
        result = subtract_matrices(matrix_c, matrix_a)
    except ValueError:
        return None
    if result is not None:
        print(f"\n{result}")

def mul_AB2():
    matrix_a = np.array([1, 0, -3, 2, 4, 1]).reshape(2, 3)
    matrix_b = np.array([1, 0, 4, 1, -2, 3, -1, 5, 0, -1, 2, 1]).reshape(3, 4)
    try:
        result = multiply_matrices(matrix_a, matrix_b)
    except ValueError:
        return None
    if result is not None:
        print(f"\n{result}")

def mul_DC():
    matrix_a = np.array([1, -2, 0, 4, -3, 1]).reshape(3, 2)
    matrix_b = np.array([2, -1, 3, 0]).reshape(2, 2)
    try:
        result = multiply_matrices(matrix_a, matrix_b)
    except ValueError:
        return None
    if result is not None:
        print(f"\n{result}")

def main():
    # part 1
    matrix_a = generate_matrix_a()
    matrix_b = generate_matrix_b()
    matrix_c = generate_matrix_c()
    matrix_d = generate_matrix_d()

    # Matrix A
    print(f"Matrix A:\n{matrix_a}")

    # Matrix B
    print(f"\nMatrix B:\n{matrix_b}")

    # Matrix C
    print(f"\nMatrix C:\n{matrix_c}")

    # Matrix D
    print(f"\nMatrix D:\n{matrix_d}")

    # part 2
    add_AB()
    mul_AB() # rework?
    add_FH()
    sub_CA()
    mul_AB2()
    mul_DC()

if __name__ == "__main__":
    main()