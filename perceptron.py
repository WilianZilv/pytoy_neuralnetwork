class Perceptron:

    lt = 0.01
    
    def __init__(self, input_amt):
        self.input_amt = input_amt
        self.weights = []

        for i in range(input_amt):
            self.weights.append(1)

    def guess(self, input):

        sum = 0
        for i in range(len(self.weights)):
            sum += self.weights[i] * input[i]
            
        return self.activational_function(sum)

    def train(self, input, target):

        error = target - self.guess(input)

        for i in range(len(self.weights)):
            self.weights[i] +=  error * input[i] * self.lt

    def activational_function(self, sum):

        if sum >= 1:
            return 1
        else:
            return 0
    
