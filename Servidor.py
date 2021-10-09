from prime_gentest import*
import random

primo_seleccionado=random.choice(listaprimos)#se simula que el server entrega los datos publicos al cliente
gen_aleatorio=random.randrange(1,(primo_seleccionado-1),1)
a=random.randrange(1,(primo_seleccionado-1),1)#número aleatorio generado para generar la llave del server

#Servidor y su llave A
A=(gen_aleatorio**a)%primo_seleccionado 


with open('mensajepublico.txt', 'w') as escribir_mensaje:
    escribicion=escribir_mensaje.write("Primo= "+ str(primo_seleccionado)+' \n')
    escribicion=escribir_mensaje.write("Gen= "+ str(gen_aleatorio)+' \n')
    escribicion=escribir_mensaje.write("A= "+ str(A)+' \n')

    
print("El primo seleccionado(P) de la lista es:",primo_seleccionado)
print("El n° generado es(G): ", gen_aleatorio)#print+texto pa puro q se vea bonito
print("Pseudo key(A) del servidor es:",A)  