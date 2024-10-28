datos_personas={'Juan':[],'Florencia':[],'Martin':[]}

def menu():
    
    print('''-------Menu--------
    1) Carga de datos de una persona
    2) Calculo del promedio de altura de la persona
    3) Obtener el nombre de la persona mas pesada
    S o s) Salir del programa ''' )
    
    opc=input('Seleccione una opcion: ').lower()
    
    cadena='123s'
    
    if opc in cadena: 
        
        return opc 
    
def ingreso(k):
    
    lista=[]
    
    c=0
    while c==0:
        
        try: 
            edad=int(input(f'Ingrese la edad de {k}: '))
            
        except ValueError: 
            
            print('Ingrese una edad valida.')
            
        else: 
            
            if edad>0  and edad<130:
                c=1 
             
                lista.append(edad)
            else: 
                print('Ingrese una edad entre (0 y 130)')

    c2=0
    while c2==0:
        
        try: 
            peso=float(input(f'Ingrese el peso de {k}: '))
            
        except ValueError: 
            print('Ingrese el peso como numero.')
            
        else: 
            
            if peso>=30 and peso<=180:
                
                c2=1 
                
                lista.append(peso)
                
            else: 
                print('ingrese un peso en KG entre [30 y 180]')
                


    c1=0
    while c1==0:

        try: 
             
            altura=float(input('Ingrese la altura en metros: ')) 
            
            
        except ValueError: 
            
            print('Ingrese un numero!')
            
        else: 
            
            if altura>=0 and altura<=2.30:
                
                c1=1 
                lista.append(altura)
            else: 
                print('Ingrese una altura entre [0 y 2.30]')                

    datos_personas[k]=lista
    print(datos_personas)
    
    return True

def promedio_altura(dicc):
    alturas=0
    for i in dicc: 
        
        alturas+=dicc[i][2]
        
    
    prom=alturas/len(dicc)
    
    return prom 



def mas_pesado(dicc):
    
    mayor=0
    
    for i in dicc: 
        
        
       
        if dicc[i][1]>mayor:
           
            mayor=dicc[i][1]
            
            nombre=i    
    
    return nombre 
        

    

validacion=False 
b=0
while b==0:
    
    op=menu()
    
    if op=='1':
        b1=0
        
        while b1==0:
         
            clave=input('Ingrese una clave: ').capitalize()
         
            if clave in datos_personas:

                b1=1

                validacion=ingreso(clave)
                
            else:
                
                print('Intente con una clave valida')
                print(datos_personas)
         
            
        
        print('Ingreso')
        
    elif op=='2' and validacion==True:
        
        promedio=promedio_altura(datos_personas)
        
        print(f'El promedio de alturas es: {promedio}')
        
    elif op=='3' and validacion==True:
         
        pesado=mas_pesado(datos_personas)
            
        print(f'La persona mas pesada es {pesado} ')        
    elif op=='s':
        print('Saliendo del programa. Hasta luego.')
        b=1
    else: 
        
        print('Opcion incorrecta. Reintente')
        print('''
              
              
              ''')