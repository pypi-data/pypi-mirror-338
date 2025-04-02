import numpy as np

class Helper:
    def __init__(self):
        pass

    def set_vector(self, arr1: list, arr2: list):
        self.a = np.array(arr1)
        self.b = np.array(arr2)
    
    def set_matrix(self, arr: list):
        self.mat = np.array(arr)
    
    def set_eigen(self):
        self.eVal, self.eVec = np.linalg.eig(self.mat)

    def cal_dot(self):
        return self.a@self.b

    def cal_rad(self):
        try: return (self.cal_dot)/(np.linalg.norm(self.a-self.b))
        except: return 0.0
    
    def cal_deg(self):
        try: tmp = (self.cal_dot)/(np.linalg.norm(self.a-self.b))
        except: tmp = 0.0
        return np.rad2deg(np.arccos(tmp))

    def cal_diag(self):
        return np.diag([self.eVal[1], self.eVal[0]])

    def cal_stack(self):
        return np.column_stack((self.eVec[:,1], self.eVec[:,0]))
    
    def print_matrix(self):
        return self.mat
    
    @staticmethod
    def cal_inverse(a):
        return np.linalg.inv(a)
    