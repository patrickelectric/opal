from dev.paropt import Algorithm
from dev.paropt import Parameter
from dev.paropt import Measure

class GFCompAlg(Algorithm):
    '''
    This class define growth factor computing algorithm that
    considers that the input matrix as the parameters. For example 
    we want to compute the growth factor of a matrix 3x3, we 
    will use an algorithm that has 9 parameters, each parameter 
    represents for a cell of matrix
    '''
    def __init__(self,matrixSize=0,**kwargs):
        Algorithm.__init__(self,name='GFC',purpose='Compute growth factor of a matrix')
        self.matrix_size = matrixSize
        # Add the parameters, each parameter corresponds to a cell of matrix
        for i in range(self.matrix_size):
            self.add_param(Parameter(name='CELL'+str(i),kind='real',default=1.0))
        
        # Define the measures
        self.add_measure(Measure(name='GF',kind='real',description='Growth factor of Gaussian Elimination on the matrix'))
        return

    def set_parameter(self,parameters):
        f = open(self.parameter_file,'w')
        for param in parameters:
            f.write(str(param.value) + ' ')
        f.write('\n')
        f.close()
        return
