import pandas as pd
import matplotlib.pyplot as plt
from generator.generadorICA import generarDatosICA

def contruirDataIca():

    #Creando dataFrame

    datosIca = generarDatosICA()
    dataFrameIca = pd.DataFrame(datosIca, columns=['comuna', 'ica', 'fecha', 'id'])
    dataFrameIca.to_csv('DatosIca.csv', index=False)
    print(dataFrameIca)
    #Generando gráfica de los datos por promedio de comuna
    DatosOrdenadosPorComuna = dataFrameIca.groupby("comuna")["ica"].mean()
    plt.figure(figsize=(20,20))
    DatosOrdenadosPorComuna.plot(kind='bar', color='blue')
    plt.show()



contruirDataIca()

