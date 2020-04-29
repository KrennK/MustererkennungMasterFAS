import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def step_one():
    '''
    Schritt 1: Lesen Sie mit Hilfe von Pandas die Daten aus 'ImportFiles/2d_samples.csv' ein und geben Sie die ersten fünf Datensätze aus!
    '''
    
    data = pd.read_csv("ImportFiles/2d_samples.csv", header=0)
    data.set_index("Label", inplace=True)
    data.head()

    return data

def step_two(data):
    '''
    Schritt 2: Erstellen Sie mit Matplotlib ein Histogramm aus dem ersten Merkmal x1!
    Hinweis: Verwenden Sie die Funktion hist()!
    Quelle: https://www.python-kurs.eu/matplotlib_histogramme.php
            https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.hist.html
    '''

    # extract first value
    X1 = data.loc['A','x1'].values
    X2 = data.loc['B','x1'].values

    plt.hist([X1],bins=20, alpha=0.8)
    plt.hist([X2],bins=20, alpha=0.8)
    plt.show()

def step_three(data):
    '''
    Schritt 3: Erstellen Sie mit Matplotlib einen Scatterplot mit beiden Merkmalen x1 und x2!
    Hinweis: Verwenden Sie die Funktion scatter()!
    Quelle: https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
    '''

    #extract values
    X = data.iloc[:, [0,1]].values
    
    #plot data
    plt.scatter(X[:1000, 0], X[:1000, 1], color='red', marker='o', label='A')
    plt.scatter(X[1000:1500, 0], X[1000:1500, 1], color='blue', marker='x', label='B')
    plt.scatter(data['x1'],data['x2'], marker='o', alpha=0.5)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    data = step_one()
    step_two(data)
    step_three(data)