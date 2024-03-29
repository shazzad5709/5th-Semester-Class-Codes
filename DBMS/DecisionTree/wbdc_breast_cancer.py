import numpy as np
import pandas as pd
from test import train_and_test
from numpy import genfromtxt

if __name__ == '__main__':
    data = np.genfromtxt('DBMS/Datasets/BreastCancer/wdbc.csv', delimiter=',')
    data = data[:,1:]
    data[:,[30,0]]=data[:,[0,30]]
    X, y = data[:, 0:-1], data[:, -1]

    features = [
        'mean radius', 'mean texture', 'mean perimeter', 'mean area',
        'mean smoothness', 'mean compactness', 'mean concavity',
        'mean concave points', 'mean symmetry', 'mean fractal dimension',
        'radius error', 'texture error', 'perimeter error', 'area error',
        'smoothness error', 'compactness error', 'concavity error',
        'concave points error', 'symmetry error',
        'fractal dimension error', 'worst radius', 'worst texture',
        'worst perimeter', 'worst area', 'worst smoothness',
        'worst compactness', 'worst concavity', 'worst concave points',
        'worst symmetry', 'worst fractal dimension'
    ]

    classes = {1: 'Bening', 0: 'Malignant'}

    train_and_test(X, y, classes, features)