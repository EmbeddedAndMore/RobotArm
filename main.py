import sys
import numpy as np
from boxstack import BoxStack





if __name__ == "__main__":

    if len(sys.argv) == 4:
        box = BoxStack(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        coord = box.box_coordinate(2, 0, 2)
        print(f"X:{coord[0]}\nY:{coord[1]}\nZ:{coord[2]}")
    elif len(sys.argv) == 7:
        box = BoxStack(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
        coord = box.box_coordinate(int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]))
        print(f"X:{coord[0]}\nY:{coord[1]}\nZ:{coord[2]}")
    else:
        box = BoxStack(500,200,300)
        coord = box.box_coordinate(2, 0, 2)
        print(box.box.shape)
        print(f"X:{coord[0]}\nY:{coord[1]}\nZ:{coord[2]}")



