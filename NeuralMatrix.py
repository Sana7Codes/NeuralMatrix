import numpy as np

class MatrixIsSingular(Exception):
    """Custom exception for singular matrices"""
    pass

class NeuroMatrixAnalyzer:  
    def __init__(self, weight_matrix):  
        self.weights = np.array(weight_matrix, dtype=np.float32)  

    def check_trainability(self):  
        """Ensure neural network weight matrix is non-singular"""  
        try:  
            if is_singular(self.weights):  
                raise MatrixIsSingular("Network untrainable: Singular weight matrix")  
            return "Stable network"  
        except MatrixIsSingular:  
            return "Apply dropout or regularization"  

    def synaptic_pruning(self, threshold=0.1):  
        """Simulate biological pruning of weak neural connections"""  
        self.weights = np.where(self.weights < threshold, 0, self.weights)  
        return self.weights  

def is_singular(matrix, tol=1e-6):  
    """Check if matrix is singular using determinant"""  
    return np.linalg.cond(matrix) > 1/tol  # High condition number means near-singular