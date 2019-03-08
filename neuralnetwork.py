from matrix import Matrix
import math
import random

class NeuralNetwork:

    def __init__(self, input_amt, hidden_amt, output_amt):

        self.lr = 0.1
        self.input_amt = input_amt
        self.hidden_amt = hidden_amt
        self.output_amt = output_amt

        self.weights_ih = Matrix(hidden_amt, input_amt)
        self.weights_ho = Matrix(output_amt, hidden_amt)

        self.bias_h = Matrix(hidden_amt, 1)
        self.bias_o = Matrix(output_amt, 1)

    def predict(self, input_array):

        inputs = Matrix.from_array(input_array)
        
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)

        hidden.map(NeuralNetwork.sigmoid)

        output = Matrix.multiply(self.weights_ho, hidden)
        output.add(self.bias_o)
        output.map(NeuralNetwork.sigmoid)

        return Matrix.to_array(output)

    def train(self, input_array, targets_array):
        
        inputs = Matrix.from_array(input_array)
        
        hidden = Matrix.multiply(self.weights_ih, inputs)
        hidden.add(self.bias_h)

        hidden.map(NeuralNetwork.sigmoid)

        outputs = Matrix.multiply(self.weights_ho, hidden)
        outputs.add(self.bias_o)
        outputs.map(NeuralNetwork.sigmoid)
        
        targets = Matrix.from_array(targets_array)
        
        outputs_errors = Matrix.subtract(targets, outputs)

        gradients = Matrix.map_matrix(outputs, self.dsigmoid)
        gradients = Matrix.multiply(gradients, outputs_errors)
        gradients.multiply_self(self.lr)

        self.bias_o = Matrix.add_matrix(self.bias_o, gradients)

        hidden_t = Matrix.transpose(hidden)
        weight_ho_deltas = Matrix.multiply(gradients, hidden_t)

        self.weights_ho = Matrix.add_matrix(self.weights_ho, weight_ho_deltas)

        weights_t = Matrix.transpose(self.weights_ho)
        hidden_errors = Matrix.multiply(weights_t, outputs_errors)

        hidden_gradient = Matrix.map_matrix(hidden, self.dsigmoid)
        hidden_gradient = Matrix.multiply(hidden_gradient, hidden_errors)
        hidden_gradient.multiply_self(self.lr)

        self.bias_h = Matrix.add_matrix(self.bias_h, hidden_gradient)

        inputs_t = Matrix.transpose(inputs)
        weight_ih_deltas = Matrix.multiply(hidden_gradient, inputs_t)

        self.weights_ih = Matrix.add_matrix(self.weights_ih, weight_ih_deltas)

    def mutate(self):

        def func(x):

            offset = random.randrange(-10, 10) * .001
            new_x = x + offset
            return new_x


        self.weights_ih.map(func);
        self.weights_ho.map(func);
        self.bias_h.map(func);
        self.bias_o.map(func);

    def reset(self):

        def func(x):
            return 0

        self.weights_ih.map(func);
        self.weights_ho.map(func);
        self.bias_h.map(func);
        self.bias_o.map(func);
    
    @staticmethod
    def sigmoid(x):
        return 1 / (1 + math.exp(-x))

    @staticmethod
    def dsigmoid(y):
        return y * (1-y)
