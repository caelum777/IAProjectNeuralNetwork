__author__ = 'Pablo'
import numpy as np

class NeuralNetwork():

    def __init__(self):
        self.inputs = [[0, 0, 0, 0, 1, 1, 1, 1]]
        self.outputs = [[0, 1, 0]]
        self.W1 = []
        self.W2 = []
        self.hidden_layer_neurons = 7
        self.output_layer_neurons = 3
        self.hidden_layer = []
        self.output_layer = []
        self.alpha = 0.4

    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))

    #  hidden layer
    def feed_forward(self, inputs):
        inputs = self.inputs #parche
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

        #print "Hidden layer output: " + str(self.hidden_layer)
        #print "Output: " + str(self.output_layer[0])
        self.back_propagation()

#BackPropagation, possibly bugged, still on development
    def back_propagation(self):
        newW2 = self.W2[:]
        for i, output in enumerate(self.output_layer[0]):
            if self.outputs[0][i] == 1:
                delta = output * (1 - output) * (self.outputs[0][i] - output)
                for y, w2 in enumerate(newW2[i]):
                    newW2[i][y] = w2 + self.alpha * self.hidden_layer[0][y] * delta
                #print self.W1
                for x, l in enumerate(self.W1):
                    #print "Hiddenresult = "+str(self.hidden_layer[0][x])
                    #print "peso2 = "+str(self.W2[i][x])
                    #print delta
                    d2 = self.hidden_layer[0][x] * (1 - self.hidden_layer[0][x]) * (self.W2[i][x] * delta)
                    #print "D"+str(x) +"= "+str(d2)
                    #print "---------------------------"
                    for y, w1 in enumerate(l):
                        #print "W1"+str(x)+str(y)+"=?"
                        self.W1[x][y] = w1 + self.alpha * self.inputs[0][y] * delta
        self.W2 = newW2[:]
        #print self.W1
        #print self.hidden_layer

        #print self.W2
        #print self.W1
        #for i in self.W2:
        #    print i
        #self.W2
