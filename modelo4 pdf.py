datos={}

def menu():
    
    print('''----Menu----
          1) Cargar datos de un dia/mes [temperatura y presion]
    2) Listar los valores cargados (un dia por linea)
    3) Buscar prediccion
    f) finalizar''')
    
    opc=input('Ingrese una opcion: ').lower()
    
    return opc 


def carga():
    
    lista=[]
    
    c=0
    while c==0:
        try: 
            dia=int(input('Ingrese el dia: '))
        except ValueError: 
            print('Error. Debe ingresar un numero')
            
        else: 
            
            if dia>0 and dia<=30:
               
                c=1
            
            else: 
                
                print('''Debe ingresar un dia valido. Reintente 
                      
                      ''')
                
    c1=0 
    while c1==0:
        try: 
            mes=int(input('Ingrese el mes: '))
        
        except ValueError:
            print('Error. Debe ingresar el mes como numero')
            
        else: 
            
            if mes>0 and mes<=12:
                
                c1=1 
            
            else: 
                
                print('''Ingrese un mes valido
                      ''')
    
    clave=(f'{dia}/{mes}')
    
    
    if clave in datos:
        
        print('El dia y el mes ya se encuentran cargados')
        
   
    else: 

    
        c2=0
        while c2==0:
            try: 
                t=float(input('Ingrese la temperatura: '))
            
            except ValueError: 
                print('Intente con un numero')
                print(' ')
                
            else: 
                
                if t>=-10 and t<=55:
                    
                    c2=1 
                    
                else: 
                    print('Error. Debe Ingresar una temperatura en el rango [-10,55]')
        
        c3=0
        while c3==0:
            
            try: 
                p=float(input(f'Ingrese la presion de {clave}: '))
            
            except ValueError: 
                print('Intente escribiendo la presion como numero')
                
                print(' ')
                
            else: 
                
                if p>=760 and p<=960:
                    c3=1 
                else: 
                    print('Ingrese una presion valida')
                    
                
        lista.append(t)
        lista.append(p)
        
        datos[clave]=lista 
   
    return True        

def listar(dicc):
     
     for i in datos:
         print(i,':', datos[i])
    
    
def prediccion(datos):
    
    for i in datos: 
        
        if (datos[i][0]>25) and datos[i][1]<800:
            print(f'El dia {i} deberia llover')
        else: 
            print('No esta pronosticado lluvia')
            
    




validacion= False
b=0
while b==0:
    
    op=menu()
    
    if op=='1':
        
        validacion=carga()
        
    elif op=='2' and validacion==True:
        
        listar(datos)
        
    elif op=='3' and validacion==True:
        prediccion(datos)
    
    elif op=='f':
        print('''Saliendo del programa
              Hasta luego 
              ''')
        b=1
    else: 
        print(''' Opcion incorrecta. Reintente
              
              ''')