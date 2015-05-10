__author__ = 'Andres'

__author__ = 'Andres'
import numpy as np


inputs = [[0, 0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 1, 1, 1, 1, 1]]
outputs = [[0, 0, 0, 0, 1, 1, 1, 0]]
W1 = []
W2 = []
hidden_layer_neurons = 7
output_layer_neurons = 3
hidden_layer = []
output_layer = []


def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

#  hidden layer
for i, input in enumerate(inputs):
    hidden_layer.append([])
    for x in range(0, hidden_layer_neurons):
        W1.append(np.random.randn(1, len(input))[0])
        hidden_input = 0
        for y in range(0, len(input)):
            hidden_input += W1[x][y] * input[y]
        hidden_layer[i].append(sigmoid(hidden_input))

#  output layer
for i, input in enumerate(inputs):
    output_layer.append([])
    for x in range(0, output_layer_neurons):
        W2.append(np.random.randn(1, hidden_layer_neurons)[0])
        output_layer_input = 0
        for y in range(0, hidden_layer_neurons):
            output_layer_input += W2[x][y] * hidden_layer[i][y]
        output_layer[i].append(sigmoid(output_layer_input))

# print "Hidden layer output: " + str(hidden_layer)
print "Output: " + str(output_layer[0])
