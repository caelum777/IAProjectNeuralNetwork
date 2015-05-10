__author__ = 'Pablo'
import numpy as np

class NeuralNetwork():

    def __init__(self):

        inputs = [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1]]
        self.outputs = [[0, 0, 0, 0, 1, 1, 1, 0]]
        self.W1 = []
        self.W2 = []
        self.hidden_layer_neurons = 7
        self.output_layer_neurons = 3
        self.hidden_layer = []
        self.output_layer = []

    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))

    #  hidden layer
    def feed_forward(self, inputs):
        for i, input in enumerate(inputs):
            self.hidden_layer.append([])
            for x in range(0, self.hidden_layer_neurons):
                self.W1.append(np.random.randn(1, len(input))[0])
                hidden_input = 0
                for y in range(0, len(input)):
                    hidden_input += self.W1[x][y] * input[y]
                self.hidden_layer[i].append(self.sigmoid(hidden_input))

        #  output layer
        for i, input in enumerate(inputs):
            self.output_layer.append([])
            for x in range(0, self.output_layer_neurons):
                self.W2.append(np.random.randn(1, self.hidden_layer_neurons)[0])
                output_layer_input = 0
                for y in range(0, self.hidden_layer_neurons):
                    output_layer_input += self.W2[x][y] * self.hidden_layer[i][y]
                self.output_layer[i].append(self.sigmoid(output_layer_input))

        print "Hidden layer output: " + str(self.hidden_layer)
        print "Output: " + str(self.output_layer[0])
