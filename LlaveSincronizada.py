# Universidad Finis Terrae, Laboratorio Evaluado n°2 (lab4)
# Profesor: Manuel Alba
# Estudiantes: Miguel Orellana | Ismael Solis
# Fecha de entrega: 6 de octubre 2021

from Servidor import*
from Cliente import*

K1=(B**a)%primo_seleccionado
K2=(A**b)%primo_seleccionado

if K1!=K2:
    print("Las llaves no estan sincronizadas, coloque los valores correspondientes que aparecen en la consola, la llave privada del servidor es", 
          K1,"y la del cliente es",K2 ,", por favor reinicie el programa")
else:
    print("Las llaves estan sincronizadas, la llave privada del servidor es", K1, "y la llave del cliente es", K2)
    