import pytest
import numpy as np
from boxstack import BoxStack

def test_box_coordinate():
    box = BoxStack(500, 200, 300)
    coord = box.box_coordinate(0,0,0)
    assert np.array_equal(coord, np.array([250,0,0])) == True

    coord = box.box_coordinate(1,1,1)
    assert np.array_equal(coord, np.array([750,200,300])) == True


    coord = box.box_coordinate(-1,0,0)
    assert np.isnan(coord).any() == True