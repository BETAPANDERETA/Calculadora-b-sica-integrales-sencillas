#----------------------------------
# Calculadora básica de integrales|
# AUTOR: BETAPANDERETA            |
# Version: 0.5.5                  |
#----------------------------------

def create_table(i,xi,f_xi,area):

    labels = "|i||       Xi         ||      f(Xi)       |"
    info = "|"+str(i)+"||"+str(xi)+"||"+str(f_xi)+"|"
    resultado = "|        ÁREA:        ||"+str(area)+"|"

    tabla = [labels,info,resultado]

    return tabla

def data_entry():

    n = int(input("n:"))
    
    while True:
        
        a = float(input("a:"))
        b = float(input("b:"))
        
        labels = "|          n:"+str(n)+"       ||     I["+str(int(a))+","+str(int(b))+"]       |"
        print(labels)

        if b > a and b != a:

            data = [n,a,b]
            return data
            False

        else: print("¡a > b!")

def func_num(x):  #Función numérica

    #----------------------------------
    # Funciones de prueba
    # e = 2.71828    
    # f = pow(e,x)  
    # f = pow(x,2)
    #----------------------------------

    f = 1/x  # Función racional f(x) = 1/x puede cambiarse 
    return f

def aprox_der():

    ent = data_entry()

    delta_x = (ent[2]-ent[1])/(ent[0])
    x_i = ent[1]
    f_xi = 0
    sum = 0
    i = 0

    tabla_labels = create_table(i,x_i,f_xi,0)
    print(tabla_labels[0])

    for i in range (ent[0]):
        
        x_i += delta_x
        f_xi = func_num(x_i)
        sum += f_xi
        
        # Creando la tabla en la terminal

        tabla_info = create_table(i+1,x_i,f_xi,0)
        print(tabla_info[1])

    area = sum*delta_x

    tabla_rs = create_table(i+1,x_i,f_xi,area)
    print(tabla_rs[2])

def aprox_simp():

    ent = data_entry()

    delta_x = (ent[2]-ent[1])/(ent[0])
    x_i = ent[1]
    f_xi = func_num(x_i)
    sum = 0
    i = 0

    tabla_labels = create_table(i,x_i,f_xi,0)
    print(tabla_labels[0])
    print(tabla_labels[1])

    for i in range (ent[0]):
        
        x_i += delta_x

        if i%2 == 0:
            f_xi = 2*func_num(x_i)
        else: 
            f_xi = 4*func_num(x_i)

        if i == ent[0]:
            f_xi = func_num(x_i)
  
        sum += f_xi
        
        # Creando la tabla en la terminal

        tabla_info = create_table(i+1,x_i,f_xi,0)
        print(tabla_info[1])

    area = sum*((1/3)*delta_x)

    tabla_rs = create_table(i+1,x_i,f_xi,area)
    print(tabla_rs[2])

aprox_der()
aprox_simp()