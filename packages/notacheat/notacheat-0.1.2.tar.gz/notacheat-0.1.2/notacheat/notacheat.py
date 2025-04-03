import numpy as np

class Helper:
    def __init__(self):
        self.a = None
        self.b = None
        self.mat = None
        self.eVal = None
        self.eVec = None

    def set_vector(self, arr1: list, arr2: list):
        self.a = np.array(arr1)
        self.b = np.array(arr2)
    
    def set_matrix(self, arr: list):
        self.mat = np.array(arr)
        self.eVal, self.eVec = np.linalg.eig(self.mat)

    def dot(self):
        return self.a@self.b

    def rad(self):
        try:
            return (self.dot())/(np.linalg.norm(self.a-self.b))
        except:
            return 0.0
    
    def deg(self):
        return np.rad2deg(np.arccos(self.rad()))

    def diag(self):
        return np.diag([self.eVal[1], self.eVal[0]])

    def stack(self):
        return np.column_stack((self.eVec[:,1], self.eVec[:,0]))
    
    def matrix(self):
        return self.mat
    
    @staticmethod
    def inverse(a):
        try:
            return np.linalg.inv(a)
        except:
            return 0.0
