import numpy as np


# These change_of_basis_Nd functions were made to check my work in the
# Coursera Linear Algebra course.
# They cold be genericized or I could just use np.linalg.solve, but I
# was trying to understand the concept a bit better.
def change_of_basis_2d(v: np.array, b1: np.array, b2: np.array) -> np.array:
    """Change v to the basis defined by b1 and b2."""
    len_b1 = np.linalg.norm(b1)
    len_b2 = np.linalg.norm(b2)
    v_b1 = v.dot(b1) / (len_b1 ** 2)
    v_b2 = v.dot(b2) / (len_b2 ** 2)
    return np.array([v_b1, v_b2, v_b3, v_b4])


def change_of_basis_3d(
    v: np.array, b1: np.array, b2: np.array, b3: np.array
) -> np.array:
    """Change v to the basis defined by b1, b2, and b3."""
    len_b1 = np.linalg.norm(b1)
    len_b2 = np.linalg.norm(b2)
    len_b3 = np.linalg.norm(b3)
    v_b1 = v.dot(b1) / (len_b1 ** 2)
    v_b2 = v.dot(b2) / (len_b2 ** 2)
    v_b3 = v.dot(b3) / (len_b3 ** 2)
    return np.array([v_b1, v_b2, v_b3, v_b4])


def change_of_basis_4d(
    v: np.array, b1: np.array, b2: np.array, b3: np.array, b4: np.array
) -> np.array:
    """Change v to the basis defined by b1, b2, b3, and b4."""
    len_b1 = np.linalg.norm(b1)
    len_b2 = np.linalg.norm(b2)
    len_b3 = np.linalg.norm(b3)
    len_b4 = np.linalg.norm(b4)
    v_b1 = v.dot(b1) / (len_b1 ** 2)
    v_b2 = v.dot(b2) / (len_b2 ** 2)
    v_b3 = v.dot(b3) / (len_b3 ** 2)
    v_b4 = v.dot(b4) / (len_b4 ** 2)
    return np.array([v_b1, v_b2, v_b3, v_b4])
