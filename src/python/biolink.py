import numpy as np
import ctypes


clibrary = ctypes.CDLL("./src/lib/biolink.so")

normalize = clibrary.normalize
normalize.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int, ctypes.c_double]
normalize.restype = ctypes.c_int

clear_matrix = clibrary.clear_matrix
clear_matrix.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int, ctypes.c_double, ctypes.c_double, ctypes.c_double]
clear_matrix.restype = ctypes.c_int

remove_dependence = clibrary.remove_dependence
remove_dependence.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int, ctypes.c_int, ctypes.c_int]
remove_dependence.restype = ctypes.c_int


class Matrix:
	def __init__(self, array):
	    array = np.transpose(array)
	    self.rows, self.cols = array.shape
	    self.matrix = (ctypes.c_double * (self.rows * self.cols))(*array.flatten())

	def normalize(self, c):
		normalize(self.matrix, self.rows, self.cols, c)

	def clear_matrix(self, min_mean, max_mean, min_variance):
		self.rows = clear_matrix(self.matrix, self.rows, self.cols, min_mean, max_mean, min_variance)
		self.matrix = (ctypes.c_double * (self.rows * self.cols))(*self.matrix[:(self.rows * self.cols)])

	def remove_dependence(self, new_rows):
	    self.rows = remove_dependence(self.matrix, self.rows, self.cols, new_rows)
	    self.matrix = (ctypes.c_double * (self.rows * self.cols))(*self.matrix[:(self.rows * self.cols)])
	    
	def pca(self, new_rows):
	        mean = np.mean(self.to_array(), axis=0)
	        centered_data = self.to_array() - mean
	        
	        cov_matrix = np.cov(centered_data.T)
	        eigen_values, eigen_vectors = np.linalg.eigh(cov_matrix)
	        
	        index = np.argsort(eigen_values)[::-1]
	        eigen_values = eigen_values[index]
	        eigen_vectors = eigen_vectors[:, index]
	        
	        eigen_vectors = eigen_vectors[:, :new_rows]
	        projected_data = np.dot(centered_data, eigen_vectors)
	        
	        self.rows = new_rows
	        self.matrix = (ctypes.c_double * (self.rows * self.cols))(*projected_data.flatten())

	def to_array(self):
	    return np.transpose(np.ctypeslib.as_array(self.matrix).reshape(self.rows, self.cols))

