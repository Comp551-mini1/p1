import numpy as np
import pandas as pd

class knn(object):
    
    def __init__(self, x, y):
        self.x_train = x
        self.y_train = y

    def predict(self, x, k):
        
    
