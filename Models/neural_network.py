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
        self.W1 = []
        self.W2 = []
        self.hidden_layer_neurons = 624
        self.output_layer_neurons = 36
        self.hidden_layer = []
        self.output_layer = []
        self.alpha = 0.4

    def variable_initialization(self, inputs):
        #  inputs = self.inputs #  parche
        flag = 0
        self.hidden_layer.append([])
        #  print inputs[0]
        for x in range(0, self.hidden_layer_neurons):
            self.W1.append(np.random.randn(1, len(inputs))[0])
        #print len(self.W1[0])
        for x in range(0, self.output_layer_neurons):
            self.W2.append(np.random.randn(1, self.hidden_layer_neurons)[0])
        #print len(self.W2)

    def sigmoid(self, z):
        return 1.0/(1.0+np.exp(-z))

    #    hidden layer
    def feed_forward(self, input):
        print "Plz w8 iniciando feedfoward"
        #  inputs = self.inputs #  parche
        self.hidden_layer.append([])
        for x in range(0, self.hidden_layer_neurons):
            #  self.W1.append(np.random.randn(1, len(input))[0])
            hidden_input = 0
            #for y in range(0, len(input)):
            hidden_input += self.W1[x][0] * input[0]
            self.hidden_layer[0].append(self.sigmoid(hidden_input))
            #  print self.sigmoid(hidden_input)

        #    output layer
        for x in range(0, self.output_layer_neurons):
            #  self.W2.append(np.random.randn(1, self.hidden_layer_neurons)[0])
            output_layer_input = 0
            for y in range(0, self.hidden_layer_neurons):
                output_layer_input += self.W2[x][y] * self.hidden_layer[0][y]
            self.output_layer.append(self.sigmoid(output_layer_input))
            #  print self.sigmoid(output_layer_input)

        #  print "Hidden layer output: " + str(self.hidden_layer)
        #  print "Output: " + str(self.output_layer[0])
        #print self.inputs
        self.inputs = input
        self.back_propagation()
        #print "res: ", self.W2
        print self.output_layer
        self.hidden_layer = []
        self.output_layer = []

#  BackPropagation, possibly bugged, still on development
    def back_propagation(self):
        print "Plz w8 inicializando backpropagation"
        newW2 = self.W2[:]
        for i, output in enumerate(self.output_layer):
            if self.outputs[i] == 1:
                delta = output * (1 - output) * (self.outputs[i] - output)
                for y, w2 in enumerate(newW2[i]):
                    newW2[i][y] = w2 + self.alpha * self.hidden_layer[0][y] * delta
                #  print self.W1
                for x, l in enumerate(self.W1):
                    #  print "Hiddenresult = "+str(self.hidden_layer[0][x])
                    #  print "peso2 = "+str(self.W2[i][x])
                    #  print delta
                    d2 = self.hidden_layer[0][x] * (1 - self.hidden_layer[0][x]) * (self.W2[i][x] * delta)
                    #  print "D"+str(x) +"= "+str(d2)
                    #  print "---------------------------"
                    for y, w1 in enumerate(l):
                        #  print "W1"+str(x)+str(y)+"=?"
                        #  print self.W1[x][y]
                        #  print self.inputs[0][y]
                        self.W1[x][y] = w1 + self.alpha * self.inputs[y] * delta
        self.W2 = newW2[:]
        #  print self.W1
        #  print self.W2
        #  print self.W1
        #  print self.hidden_layer

        #  print self.W2
        #  print self.W1
        #  for i in self.W2:
        #      print i
        #  self.W2
