class Network():
    ''' implements a neural network '''
    def __init__(self, layer_sizes):
        ''' layer_sizes is a normal python array (not a numpy ndarray) where
            each element is the number of neurons in that layer of the net '''
        self.layer_sizes = layer_sizes
        self.weights = []
        self.biases = []

    def sgd(self):
        ''' implements learning through stochastic gradient descent '''
