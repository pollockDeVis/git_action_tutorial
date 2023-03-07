import pytest

import numpy as np

import pytest_code
 
def test_area():
    output = pytest_code.area_of_rectangle(2,5)
    assert output == 10
 
def test_perimeter():
    output = pytest_code.perimeter_of_rectangle(2,5)
    assert output == 14
    