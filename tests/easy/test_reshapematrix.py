import pytest
from easy.reshapematrix import matrixReshape


def test_reshapematrix():
    mat, r, c = [[1, 2], [3, 4]], 1, 4
    assert (matrixReshape(mat, r, c)) == [[1, 2, 3, 4]]


def test_reshapematrix1():
    mat, r, c = [[1, 2], [3, 4]], 2, 4
    assert (matrixReshape(mat, r, c)) == [[1, 2], [3, 4]]
