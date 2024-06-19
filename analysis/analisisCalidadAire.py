import pandas as pd
from generator.generadorICA import generarDatosICA

def contruirDataIca():

    #Creando dataFrame

    datosIca = generarDatosICA()
    dataFrameIca = pd.DataFrame(datosIca, columns=['comuna', 'ica', 'fecha', 'id'])
    dataFrameIca.to_csv('DatosIca.csv', index=False)
    print(dataFrameIca)

contruirDataIca()

