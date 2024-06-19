import random as rd

def generarDatosRuido():
    encuestaRuido = []
    for _ in range(2000):
        dato = {}
        id = rd.randint(1,50000)
        nivelRuido = rd.randint(10,90)
        comuna = rd.choice(['comuna 1' , 'comuna 2' , 'comuna 3' , 'comuna 4', 'comuna 5', 'comuna 6', 'comuna 7' , 'comuna 8', 'comuna 9', 'comuna 10', 'comuna 11', 'comuna 12', 'comuna 13', 'comuna 14', 'comuna 15', 'comuna 16'])
        dato =[id, nivelRuido, comuna]
        encuestaRuido.append(dato)
    return encuestaRuido
    print(encuestaRuido)

generarDatosRuido()