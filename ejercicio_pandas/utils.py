import pandas as pd

def average_of(data_frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """
        Toma un DataFrame cuyos elementos son números y, por cada columna,
        calcula el promedio.

        :param data_frame El DataFrame del cual calcular el promedio
        :type pd.DataFrame

        :param columns Las columnas de las que calcular el promedio
        :type list[str]

        :returns Un nuevo DataFrame donde las columnas originales son
                 las filas, y hay una única columna "average",
                 con el promedio de cada una.
        :rtype pd.DataFrame
    """
    # Creamos el DataFrame de promedios
    avg_data_frame = pd.DataFrame()

    # Por medio de mean() calculamos el promedio.
    # La sintaxis data_frame[columns] permite sólo considerar
    # las columnas que estén en el arreglo columns, evitando datos no numéricos.
    # Véase: https://pandas.pydata.org/docs/user_guide/indexing.html#selection-by-label
    avg_data_frame["average"] = data_frame[columns].mean()

    return avg_data_frame