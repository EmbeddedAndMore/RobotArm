import numpy as np
from numpy.core.numeric import NaN



class BoxStack:


    def __init__(self, x:int, y:int, z:int) -> None:
        """Constructor

        Args:
            x (int): box's x axis length
            y (int): box's y axis length
            z (int): box's z axis length
        """
        self.box = np.array([x,y,z])


    def update_box(self, x:int, y:int, z:int)-> None:
        """Update size of the boxes

        Args:
            x (int): box's x axis length
            y (int): box's y axis length
            z (int): box's z axis length
        """
        self.box = np.array([x,y,z])


    def box_coordinate(self, x:int, y:int, z:int) -> np.ndarray:
        """Get coordinate of left-bottom side of each box

        Args:
            x (int): 0 index location of box in X axis
            y (int): 0 index location of box in Y axis
            z (int): 0 index location of box in Z axis

        Returns:
            np.ndarray: [description]
        """
        if x<0 or y<0 or z<0:
            print("coordinate cannot be negetive")
            return np.array([np.NaN, np.NaN, np.NaN])
            
        loc    = np.array([x,y,x])
        offset = np.array([self.box[0]/2, 0, 0])

        return (loc * self.box) + offset

    
        