#----------------------------------
#| Calculadora básica de integrales|
#| AUTOR: BETAPANDERETA            |
#| Version: 0.6.0                  |
#----------------------------------
from tabulate import tabulate
import math

def tabular_data(data):

    info = data
    labels = ["i","Xi","f(Xi)"]

    tabla_info = tabulate(info,headers=labels,tablefmt="fancy_grid",disable_numparse=True)

    return tabla_info

def data_entry():

    n = int(input("n:"))
    
    while True:
        
        a = float(input("a:"))
        b = float(input("b:"))
        region = "I["+str(int(a))+","+str(int(b))+"]"

        print(tabulate([["n:",str(n),region]],tablefmt="fancy_grid"))

        if b > a and b != a:

            data = [n,a,b]
            return data
            False

        else: print("¡a > b!")

def func_num(x):  #Función numérica

    #----------------------------------
    # Funciones de prueba
    # e = 2.71828    f = 1/(math.sqrt(1+(pow(x,2)))) f = pow((pow(x,2)+8),(1/3))
    # f = pow(e,x)   f = math.sqrt(1+(pow(x,3)))     f = 1/(1+x)
    # f = pow(x,2)   f = 1/(4+(pow(x,2)))            f= 1/x
    #----------------------------------

    f = pow((pow(x,2)+8),(1/3)) # Acá poner la función deseada 

    return f

#---------------------------------------------------------
#|              Aproximación por secciones (Rn)           |
#---------------------------------------------------------

def aprox_der():

    ent = data_entry()

    delta_x = (ent[2]-ent[1])/(ent[0])
    x_i = ent[1]
    f_xi = func_num(x_i)
    sum = 0
    i = 0

    info_tabla = [[i,x_i,f_xi]]

    for i in range (ent[0]):

        x_i += delta_x
        f_xi = func_num(x_i)
        sum += f_xi
        
        #Info para construir la tabla

        data = [i+1,x_i,f_xi]
        info_tabla.append(data)
        
    area = ["AREA",sum*delta_x]
    info_tabla.append(area)

    #Creando la tabla

    imp = tabular_data(info_tabla)
    print(imp)

#---------------------------------------------------------
#|                   Regla de Simpson                      |
#---------------------------------------------------------

def aprox_simp():

    while True:

        ent = data_entry()

        if ent[0]%2 != 0:
            print("¡n Impar!")
        else:

            delta_x = (ent[2]-ent[1])/(ent[0])
            x_i = ent[1]
            f_xi = func_num(x_i)
            sum = f_xi
            i = 0

            info_tabla = [[i,x_i,f_xi]]

            for i in range (ent[0]):
                
                    x_i += delta_x

                    if i%2 != 0:
                        f_xi = 2*func_num(x_i)
                    else: 
                        f_xi = 4*func_num(x_i)

                    if i+1 == ent[0]:
                        f_xi = func_num(x_i)

                    #Info para construir la tabla

                    data = [i+1,x_i,f_xi]
                    info_tabla.append(data)

                    sum += f_xi
 
            area = ["AREA:",sum*((1/3)*delta_x)]
            info_tabla.append(area)

            #Creando la tabla

            imp = tabular_data(info_tabla)
            print(imp)

            break

#---------------------------------------------------------
#|                   Regla del Trapecio                   |
#---------------------------------------------------------

def aprox_trap():

    ent = data_entry()

    delta_x = (ent[2]-ent[1])/(ent[0])
    x_i = ent[1]
    f_xi = func_num(x_i)
    sum = f_xi
    i = 0

    info_tabla = [[i,x_i,f_xi]]

    for i in range (ent[0]):
                
        x_i += delta_x
        f_xi = 2*func_num(x_i)

        if i+1 == ent[0]:
            f_xi = func_num(x_i)
        
        sum += f_xi
                
        #Info para construir la tabla

        data = [i+1,x_i,f_xi]
        info_tabla.append(data)

    area = ["AREA",sum*((1/2)*delta_x)]
    info_tabla.append(area)

    #Creando la tabla

    imp = tabular_data(info_tabla)
    print(imp)

print("\n||            APROXIMACIÓN POR Rn          ||\n")
aprox_der()
print("\n||           APROXIMACIÓN POR SIMPSON      ||\n")
aprox_simp()
print("\n||         APROXIMACIÓN POR TRAPECIOS      ||\n")
aprox_trap()