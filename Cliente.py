from prime_gentest import*

while True:
    global primo_seleccionado
    try: 
        primo_seleccionado=int(input("Anote el número primo público(P): "))
        if primo_seleccionado==0:
            print("Valor no puede ser 0")
        elif is_prime(primo_seleccionado)==False:
            print("Valor no es primo")  
        else:
            break
    except:
        print("Input erróneo")
        
        
while True:
    global g
    try: 
        g=int(input("Anote el número generado entre 1 y el primo elegido(G): "))
        if g==0:
            print("Valor no puede ser 0")
        elif g==(primo_seleccionado):
            print("Valor no puede ser igual al primo seleccionado")
        elif g>(primo_seleccionado):
            print("Valor no puede ser mayor al primo seleccionado") 
        else:
            break
    except:
        print("Input erróneo")

while True:
    global b
    try: 
        b=int(input("Escoja un número entre 1 y el primo elegido(b):"))

        if b==0:
            print("Valor no puede ser 0")
        elif b==(primo_seleccionado):
          print("Valor no puede ser igual al primo seleccionado")
        elif b>(primo_seleccionado):
            print("Valor no puede ser mayor al primo seleccionado") 
        else:
            print("------------------------------------------------------")
            break
    except:
        print("Input erróneo")
 
        
    
B=(g**b)%primo_seleccionado #411
print("Pseudo key del cliente(B) es:", B)



