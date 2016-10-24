from utils.sort import  BubbleSort

class Knapsack:
    def __init__(self, weights=[], values=[], W=None):
        self.weights = weights
        self.values = values
        self.W = W
        self.knapsack = [0]*(W+1)

    def maximizeValue(self):
        checked = None
        for i in range(0, len(self.values)):
            v = self.values[i]
            w = self.weights[i]
            if w < self.W:
                temp = self.knapsack[w]
                if temp < v:
                    for j in range(w, len(self.knapsack)):
                        self.knapsack[j] = v
                    checked = i

        print(self.knapsack)
        if checked == len(self.values) - 1:
            print(self.knapsack[len(self.knapsack)-1])
        else:
            for i in range(checked+1, len(self.values)):
                v = self.values[i]
                w = self.weights[i]
                if w < self.W:
                    for start in range(1, len(self.knapsack)):
                        tempIndex = w + start
                        tempValue = self.knapsack[start] + v
                        #print(str(tempIndex) + ":" + str(tempValue))
                        if tempIndex < len(self.knapsack) and self.knapsack[tempIndex] < tempValue:
                            for j in range(tempIndex, len(self.knapsack)):
                                self.knapsack[j] = tempValue
                                break

            print(self.knapsack[len(self.knapsack)-1])

weights = [2,5,4]
values = [6,9,5]
W = 6
k = Knapsack(weights, values, W)
k.maximizeValue()
