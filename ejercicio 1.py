datos_personas={'Patricia':[18,88,1.75],'Juan':[19,73.5,1.80],'Jose':[55,77,1.78], 'Marta':[5,43.6,1.30]}
####Esta bien que no me muestre el promedio hasta que todo el diccionario este cargado?; 
#Como hago para usar el valor de retorno de la funcion carga para limitar que pase a 2 sin antes haber pasado por 1
def menu():
    print('''----- ---Menu--- -----
          1) Carga de Datos de una persona
          2) Calculo del promedio de altura de la persona
          3) Obtener el nombre de la persona mas pesada
          S o s) Salir del programa''')
    
    opc=input('Ingrese una opcion: ').lower()
    
    return opc


def ingreso(clave):
    
    lista=[]
    
    b1=0
    while b1==0:
        try: 
            edad=int(input(f'Ingrese la edad de {clave}: '))
            
        except ValueError: 
            print('Error. Debe ingresar un numero')
            
        else: 
            
            if edad>0:
                lista.append(edad)
                b1=1 
            else: 
                print('La edad debe ser mayor a cero')
                
    b3=0
    while b3==0:
        
        try:
            peso=float(input('Ingrese el peso del alumno: '))
            
        except ValueError: 
            print('Error. El peso debe ser un numero real!')
            
        else: 
            
            if peso>0:
                lista.append(peso)
                b3=1
                
            else: 
                
                print('Reintente la carga del peso')
                  
    b2=0
    while b2==0:
        
        try: 
            altura=float(input('Ingrese la altura del alumno: '))
            
        except ValueError: 
            print('Error. Debe ingresar un numero real para la altura.')
    
        else: 
            
            if altura>0:
                lista.append(altura)
                b2=1 
            
            else: 
                print('Error. Debe ingresar un valor mayor a 0 para la altura')
                
    datos_personas[clave]=lista

    
   
    return True


def promedio_altura(dicc):
    
    acu=0
    cont=0
    
    for i in dicc:
        
        peso=dicc[i][2]
        
        acu+=peso
        
        cont+=1 
        
    
    prom=acu/cont
    
    return prom

def mas_pesado(dicc):
    
    for i in dicc:
        peso_maxi=dicc[i][1]
            
        if dicc[i][1]>peso_maxi:
           
            peso_maxi=dicc[i][1]
            
    clave= i 
            
    
    return clave
            


####### Programa Principal########

b=0
validacion=False
while b==0:
    print(' ')
    op=menu()
    
    if op=='1':
        c=0
        
        while c==0:
            nombre=input('Ingrese el nombre de un estudiante: ')    
            
            if nombre in datos_personas:
                
                validacion=ingreso(nombre)
            
                c=1
                
                print(datos_personas)
            else: 
                print(f'El nombre "{nombre}" no se encuentra en el diccionario. Reintente')
        
        
        
        
        
    elif op=='2' and validacion==True:
        promedio_altura(datos_personas)
        
        print(f'El promedio de altura de los alumnos es: {promedio_altura(datos_personas)}')
    
    
    elif op== '3':
        
        cual=mas_pesado(datos_personas)
        
        print(f'La persona con mas peso es: {cual}')
        
    elif op=='s':
        print('Saliendo del programa. ')
        b=1
    else: 
        print('Error. Ingrese una opcion valida')
    
    
