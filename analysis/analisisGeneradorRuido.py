import pandas as pd
from generator.generadorDecibelios import generarDatosRuido

def contruirDatosRuido():

    #Creando dataFrame

    datosRuido = generarDatosRuido()
    dataFrameIca2 = pd.DataFrame(datosRuido, columns=['id', 'nivelRuido', 'comuna'])
    dataFrameIca2.to_csv('DatosRuido.csv', index=False)
    print(dataFrameIca2)


contruirDatosRuido()