import pytest
from easy.pascaltriangle import generate


def test_pascaltriangle():
    numRows,numRows1 = 5,1
    assert generate(numRows) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    assert generate(numRows1) == [[1]]