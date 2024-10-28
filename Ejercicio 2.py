
'''Un centro de investigacion biomedico necesita un programa que permita
registrar datos de tratamientos con los diferentes medicamenteos que tiene bajo 
estudio. De cada medicamento se tiene:
-Una clae de indentificacion alfanumerica
-Una descripcion
-El monto invertido en el proyecto 
-Un numero entre 1 y 30 que indica el tipo de medicamento '''

datos=[]

def menu(): #Armo la funcion menú que me retorna la opcion elegida
    
    print('''1) Carga
             2) Muestra
             3) Busca
             4) Total 
             s) S o s''')
    op=input('Ingrese una opcion: ').lower()
    
    if op in '1234s':
        
        return op
    
def carga(): #cargo un diccionario para cada índice la lista (una lista con diccionarios)
    dicc={}
    
    claveId=input('Ingrese la clave de identificacion del medicamento: ')
    
    descrip=input('Ingrese la descripcion del producto: ')

    dicc['Clave']=claveId
    dicc['descripcion']=descrip
    
    b1=0
    while b1==0:
        try: 
            monto=float(input('Ingrese el monto invertido: '))
            
        except ValueError: 
            print('Error. Debe ingresar un numero')
            
        else: 
            
            if monto>0:
                dicc['monto invertido']=monto
                
                b1=1
            else: 
                print('Reintente con un numero mayor a cero')
                print(' ')
                
    b2=0
    while b2==0:
        try: 
            numero=int(input('Ingrese el tipo de medicamento: '))
            
        except ValueError: 
            print('Intente con un numero entero.')
            
        else: 
            
            if numero>=0 and numero <=30:
                
                dicc['Tipo de medicamento']=numero
                
                b2=1
            else: 
                print('Los numeros pueden ser de [1,30]. Reintente')
                
                print(' ')
    
    datos.append(dicc)          
            
    return True #Uso para validar que cargue datos en el vector antes de realizar 

def muestra(dicc):
    
    for i in dicc: 
        print(i)
        
def buscar(datos):
    
    
    
    clave=input('Ingrese la clave: ') #Eso forma parte de la función porque no me dice que lo ponga en el programa principal
    b=0
    for i in datos: #Recorro los indices de la lista
        
        if clave==i.get('Clave'):  #Entro en el diccionario buscando el valor de la key proporcionada por el usuario
        
            print('La clave se encuentra en el diccionario')
            b=1
        
        else: 
            
            print('La clave no se encuentra en el diccionario')
    if b==1:
        
        print(i)  
    
    else: 
        
        carga() 
    

def promedio(datos):
    
    acu=0
    
    for i in datos:
        valores=i.get('monto invertido') #Acá no sé como ingresar al valor de la clave monto y sumar. 
        acu+=valores #Aparece el error "NoneType"
        
    prom=acu/len(datos)
    
    return prom
            
    


    
    
    
    
    
    
    
###Programa principal###


b=0
while b==0:
    
    opc=menu()
    
    if opc=='1':
        validar=carga()  
       
        
    elif opc=='2' and validar:
        
        muestra(datos)
        
    elif opc=='3' and validar:
        
        buscar(datos)
        
    elif opc=='4' and validar:
        
        promo=promedio(datos)
        
        print(f'El promedio invertido es: {promo}')
    
    elif opc=='s':
        print('Saliendo del programa. Hasta luego')
        
        b=1
   
    elif validar==False: 
       
        print('Primero debe cargar el un medicamento.')  #Agregue esto, pero sigue sin funcionar 
        
    else: 
        print('Ingrese una opcion correcta. ')