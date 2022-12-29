import pandas as pd
import numpy as np

def elasticidadPropia(probabilidades, beta, rangoValores):
    return beta*rangoValores*(1-probabilidades)

def elasticidadCruzada(probabilidades, beta, rangoValores):
    return -beta*rangoValores*probabilidades

def getPricesDF(rangoPrecios, medias, columnas, targetCol):

    df = pd.DataFrame(index = np.arange(rangoPrecios.size))

    for i, columna in enumerate(columnas):
        if columna is not targetCol:
            df[columna] = medias[i]

        else:
            df[targetCol] = rangoPrecios

    return df
    