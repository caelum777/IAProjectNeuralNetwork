__author__ = 'Pablo'
import numpy as np

class NeuralNetwork():

    def __init__(self):
        self.inputs = []
        self.outputs = [0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0]
        self.results = ["0", "1", "2", "3", "4", "5",
                        "6", "7", "8", "9", "A", "B",
                        "C", "D", "E", "F", "G", "H",
                        "I", "J", "K", "L", "M", "N",
                        "O", "P", "Q", "R", "S", "T",
                        "U", "V", "W", "X", "Y", "Z"]
        self.W1 = []
        self.W2 = []
        self.inputs_layer_neurons = 900
        self.hidden_layer_neurons = 624
        self.output_layer_neurons = 36
        self.hidden_layer = []
        self.output_layer = []
        self.alpha = 0.4

    def calculate_results(self):
        greater = 0
        index = 0
        for i, val in enumerate(self.output_layer):
            if val > greater:
                greater = val
                index = i
        return self.results[index]

    #  Jonathan: Made some changes, somethings weren't necessary.
    def variable_initialization(self):
        for x in range(0, self.hidden_layer_neurons):
            self.W1.append(np.random.randn(1, self.inputs_layer_neurons)[0])
        for x in range(0, self.output_layer_neurons):
            self.W2.append(np.random.randn(1, self.hidden_layer_neurons)[0])

    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))

    #    hidden layer
    def feed_forward(self, input, Tphase):
        self.hidden_layer = []
        self.output_layer = []
        for x in range(0, self.hidden_layer_neurons):
            hidden_input = 0
            for y in range(0, len(input)):
                hidden_input += self.W1[x][y] * input[y]#hidden_input += self.W1[x][0] * input[0]
            self.hidden_layer.append(self.sigmoid(hidden_input))#self.hidden_layer[0].append(self.sigmoid(hidden_input))
        #    output layer
        for x in range(0, self.output_layer_neurons):
            output_layer_input = 0
            for y in range(0, self.hidden_layer_neurons):
                output_layer_input += self.W2[x][y] * self.hidden_layer[y]
            self.output_layer.append(self.sigmoid(output_layer_input))
        self.inputs = input
        if Tphase:
            self.back_propagation()
        else:
            print "show result: ", self.calculate_results()


#  BackPropagation, IT WORKS, I guess
    def back_propagation(self):
        nw2 = self.W2[:]
        for i, output in enumerate(self.output_layer):
            if self.outputs[i] == 1 and output < 0.6:
                delta = output * (1 - output) * (self.outputs[i] - output)
                for y, w2 in enumerate(nw2[i]):
                    nw2[i][y] = w2 + self.alpha * self.hidden_layer[y] * delta
                for x, l in enumerate(self.W1):
                    d2 = self.hidden_layer[x] * (1 - self.hidden_layer[x]) * (self.W2[i][x] * delta)
                    for z, w1 in enumerate(l):
                        self.W1[x][z] = w1 + self.alpha * self.inputs[z] * d2
        self.W2 = nw2[:]
