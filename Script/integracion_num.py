#----------------------------------
#| Calculadora de integrales       |
#| AUTOR: BETAPANDERETA            |
#| BETA-INTEGRAL SOLVER            |
#| Versión: 0.7.1                  |
#----------------------------------

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tabulate import tabulate
import math
import io
import os

def tabular_data(data):

    info = data
    labels = ["i","Xi","f(Xi)"]

    tabla_info = tabulate(info,headers=labels,tablefmt="fancy_grid",floatfmt=".6f")

    return tabla_info

def data_entry():

    n = int(input("n:"))
    
    while True:
        
        a = float(input("a:"))
        b = float(input("b:"))
        region = "I["+str(int(a))+","+str(int(b))+"]"
        dx = (b - a)/n

        print(tabulate([["n",str(n),region,"Δx",str(dx)]],tablefmt="fancy_grid"))

        if b > a and b != a:

            data = [n,a,b]
            return data
            False

        else: print("¡a > b!")

def func_num(x):  #Función numérica

    f = pow((pow(x,2)+1),(1/4))  # Acá poner la función deseada 

    return f

#---------------------------------------------------------
#|              Aproximación por secciones (Rn)           |
#---------------------------------------------------------

def aprox_der():

    ent = data_entry()

    delta_x = (ent[2]-ent[1])/(ent[0])
    x_i = ent[1]
    f_xi = func_num(x_i)
    sum = f_xi
    i = 0

    info_tabla = [[i,x_i,f_xi]]

    for i in range (ent[0]):

        x_i += delta_x
        f_xi = func_num(x_i)
        sum += f_xi
        
        #Info para construir la tabla

        data = [i+1,x_i,f_xi]
        info_tabla.append(data)
        
    area = ["∑:",sum*delta_x]
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
 
            area = ["∑:",sum*((1/3)*delta_x)]
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

    area = ["∑:",sum*((1/2)*delta_x)]
    info_tabla.append(area)

    #Creando la tabla

    imp = tabular_data(info_tabla)
    print(imp)

#---------------------------------------------------------
#|                   Regla del punto medio                |
#---------------------------------------------------------

def aprox_med():

    ent = data_entry()

    delta_x = (ent[2]-ent[1])/(ent[0])
    x_i = ent[1] + (delta_x)/2
    f_xi = func_num(x_i)
    sum = f_xi
    i = 1

    info_tabla = [[i,x_i,f_xi]]

    for i in range (ent[0]-1):

        #if i == 0:
        #    x_i += (delta_x)/2

        x_i += delta_x

        f_xi = func_num(x_i)
        sum += f_xi
        
        #Info para construir la tabla

        data = [i+2,x_i,f_xi]
        info_tabla.append(data)
        
    area = ["∫f(x)dx:",sum*delta_x]
    info_tabla.append(area)

    #Creando la tabla

    imp = tabular_data(info_tabla)
    print(imp)

def plot_title():

    file = os.path.join(os.path.dirname(__file__), "Plots.txt")
    
    plot_file = open(file,"r",encoding="utf8")
    plot = plot_file.read()
    plot_file.close()

    print(plot)

def main():
    
    plot_title()

    while True:

        print("-------------------------------------------")
        opc = int(input("¿QUÉ MÉTODO DESEA USAR?\n\n ① Aprox. por particiones derechas\n ② Punto medio\n ③ Trapecios\n ④ Simpson\n 0 : CERRAR\nSu opción:"))
        print("-------------------------------------------")

        if opc == 1:
            print("\n||            APROXIMACIÓN POR Rn          ||\n")
            aprox_der()
        if opc == 2:
            print("\n||      APROXIMACIÓN POR PUNTO MEDIO       ||\n")
            aprox_med()
        if opc == 3:
            print("\n||         APROXIMACIÓN POR TRAPECIOS      ||\n")
            aprox_trap()
        if opc == 4:
            print("\n||           APROXIMACIÓN POR SIMPSON      ||\n")
            aprox_simp()

        if opc == 0:
            break

if __name__ == "__main__":
    main()