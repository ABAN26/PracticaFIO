dicc={}

def cargar():
    lista=[]

    b=0
    while b==0:

        producto=input('Ingrese el producto que desea cargar: ')
        
        if producto in dicc: 
            print('El producto ya se encuentra cargado. Intente con otro')
            
        else: 
            
            b=1 
            
            c=0 
            
            while c==0:
                 
                try:
                    mes=int(input('Ingrese el mes de vencimiento: '))
                    
                except ValueError: 
                    
                    print('Ingrese el mes en NUMEROS')
                    
                else: 
                    
                    if mes>=1 and mes<=12:
                        
                        lista.append(mes)
                        c=1 
                        
                    else: 
                        print('Ingrese un numero en el intervalo [1,12]')
                        
            c1=0
            
            while c1==0:
                try: 
                    anio=int(input('Ingrese el año de vencimiento: '))
                    
                except ValueError: 
                    
                    print('Ingrese el año en numeros!')
                    
                    
                else: 
                    
                    if anio>=2000 and anio<=2050:
                        
                        c1=1 
                        lista.append(anio)
                        
                    else: 
                        print('Ingrese un valor entre [2000,2050]')
                        
            dicc[producto]=lista 
            
            
            
        print(dicc)
        
        return True 
    
    
    
def listar():
    
    for i in dicc: 
        print(i, ':', dicc[i])
        
        
def vencer(n):
    
    for i in range(n):
        
        listar=[]
        
        for j in dicc: 
            
            if (dicc[j][0]>=7 and dicc[j][1]==2024) or (dicc[j][0]>=1 and dicc[j][0]<=7 and dicc[j][1]==2025):
                    
                listar.append(j)   #Considero que tengo que definir un intervalo de tiempo para el que conviene contar. 
                #Tomo un anio desde esta fecha 
                
    return listar   

    
def buscar(nombre):
    
    if nombre in dicc: 
        
        return [nombre, dicc[nombre]]
    
    else: 
        return False 
    
    
b=0
while b==0:
    
    print('''---- Menu ------
    1) Cargar 
    2) Listar 
    3) N productos a vencerse 
    4) Buscar un producto
    5) Finalizar''')
    
    
    op=input('Ingrese una opcion: ')
    
    if op=='1':
        
        cargar()
        
    elif op=='2':
        
        listar()
    
    elif op=='3':
        
        b5=0
        while b5==0:
            
            try: 
                num=int(input('Ingrese un numero: '))
                
            except ValueError: 
                
                print('Ingrese un entero!')
                
            else: 
                
                if num>0:
                    
                    a=vencer(num)
                    print(a)
                    b5=1 
                    
                else:
                    print('ingrese un numero positivo')
                    print(' ')
                    
                    
    elif op=='4':
        
        producto=input('ingrese el nombre del producto que esta buscando').capitalize()
        
        val=buscar(producto)
        
        if val==False:
            print('No existe el producto')
            
        else: 
            print(val)
            
            
    elif op=='5':
        print('Saliendo del programa.')
        b=1 
        
    else: 
        print('''Ingrese una opcion valida
              
              ''')
                    
                    

            
        
                
                
            
        
    
        
        
        
            
            
            
            
                        
            