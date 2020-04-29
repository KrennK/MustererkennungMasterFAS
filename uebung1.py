import pandas as pd
import matplotlib.pyplot as plt

def step_one():
    '''
    Schritt 1: Lesen Sie mit Hilfe von Pandas die Daten aus 'ImportFiles/2d_samples.csv' ein und geben Sie die ersten fünf Datensätze aus!
    '''
    
    data = pd.read_csv("ImportFiles/2d_samples.csv")

    print(data[:5])
    return data

def step_two(data):
    '''
    Schritt 2: Erstellen Sie mit Matplotlib ein Histogramm aus dem ersten Merkmal x1!
    Hinweis: Verwenden Sie die Funktion hist()!
    Quelle: https://www.python-kurs.eu/matplotlib_histogramme.php
    '''

    part = data['x1']
    plt.hist(part.values)
    plt.title("step_two: hist()")
    plt.xlabel("x1")
    plt.ylabel("value")
    plt.show()

def step_three(data):
    '''
    Schritt 3: Erstellen Sie mit Matplotlib einen Scatterplot mit beiden Merkmalen x1 und x2!
    Hinweis: Verwenden Sie die Funktion scatter()!
    Quelle: https://jakevdp.github.io/PythonDataScienceHandbook/04.02-simple-scatter-plots.html
    '''

    plt.scatter(data['x1'],data['x2'], marker='o', alpha=0.5)
    plt.title("step_three: scatterplot")
    plt.grid()
    plt.show()

if __name__ == '__main__':
    data = step_one()
    step_two(data)
    step_three(data)