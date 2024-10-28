datos={}

def menu():
        
        print('''1) Cargar datos de un dia (d,m,t,p)
              2) Listar los valores cargados 
              3) Buscar prediccion 
              f) Finalizar el programa ''')
    
        opc=input('Ingrese una opcion: ').lower()
        
        valores='123f'
        
        if opc in valores: 
           
            return opc
        

def carga():
    dicc={}
    c=0
    while c==0:
        try: 
            dia=int(input('Ingrese el dia: '))
            
        except ValueError: 
            print('Error. Debe ingresar un numero ')
            
        else: 
            
            if dia>=1 and dia<=30:
                
                c=1
                
            else: 
                print('Ingrese un dia entre [1,30]')
                
    c1=0
    while c1==0:
        try: 
            mes=int(input('Ingrese el mes: '))
            
        except ValueError: 
            print('Intente co un numero')
            
        else: 
            
            if mes>0 and mes<=12:
                c1=1 
            else:
                print('Error. Ingres un mes entre [1,12]')

    if dia and mes in datos:
        
        print('El valor ya se encuentra cargado. ')
        
    else: 
        
        dicc[dia]=dia
        dicc[dia]=mes
        
    b1=0
    while b1==0:
        try: 
            t=float(input('Ingrese la temperatura en grados centigrados: '))
            
        except ValueError: 
            print('Intente con un numero')
            
        else: 
            
            if t>=-10 and t<=55: 
                dicc['temperatura']=t
                b1=1
            
            else: 
                print('ingrese una temperatura entre [-10,55]')
    
    b2=0
    while b2==0:
        try: 
            p=float(input('Ingrese la presion atmosferica: '))
            
        except ValueError: 
            print('Intente con un numero')
            
        else: 
            
            if p>=760 and p<=960: 
                dicc['presion']=p
                b2=1 
            
            else: 
                print('ingrese la presion entre [760,960]')
                
    datos['dicc']=dicc
    print(datos)
    return datos 
 
    
 
    
###pp##

b=0
while b==0:
    
    op=menu()
    
    if op=='1':
        carga()
        
    elif op=='2':
        print('Listar')
        
    elif op=='3':
        print('Buscar prediccion')
        
    elif op=='f':
        print('Saliendo del programa. Hasta luego')
        b=1
        
    else: 
        print('Ingrese una opcion valida ')
        
        
        
        