productos={1:['vacio',4321,9],2:['costilla',6784,56],3:['nalga',3987,6]}

def menu():
    opc=input('Ingrese una opcion: ').lower()
        
    return opc 

def vender(productos):
    ventas=[]
    for i in productos:
        
        print(i, ':', productos[i])
        
 
    
    b=0 
    while b==0:
       
        elec=int(input('ingrese un producto por su ID: '))
        
        
        
        if elec in productos: 
            
            c=0
           
            while c==0:
                
                    peso= float(input(f'Ingrese la cantidad de {productos[elec]} en kg que esta vendiendo: '))
                     
                    
                    if peso>0 and peso<=1000:
                        
                        c=1 
                        
                        precio=peso*productos[elec][1]
                        
                        ventas.append(precio)
                        
                        
                    else: 
                        print('Intente con un peso valido.')
                        
                    
            
        else: 
            
            return ventas
            
            b=1
    

def labm(productos):
    
    for i in productos: 
        print(productos[i])
        

        
    print('''---Opciones
          A) Alta (Agregar un producto)
        B) Baja (Borrar)
        M) Modificar (precio por KG)--- ''')

    opc=input('Elija una opcion: ').upper()
    
    if opc=='A':
        listita=[]
        
        c=0
        while c==0:
            try: 
                
                ID=int(input('Ingrese el ID del producto: '))
            except ValueError: 
                print('Error. Debe ingresar un numero entero.')
                
            else: 
                if ID>0:
                    c=1 
                else: 
                    print('Error. El ID es un entero positivo. Reintente')
                    print(' ')
                    
                    
        producto=input('Ingrese el nombre del producto que desea agregar: ')
        
        listita.append(producto)
        
        b=0
        while b==0:
            precioxkg=float(input('Ingrese el precio por KG:  '))
            
            if precioxkg>0:
                listita.append(precioxkg)
                b=1 
            else: 
                print('Ingrese un precio positivo!!')
        
        productos[ID]=listita 
                
        
    elif opc=='B':
        
        ID=int(input('Ingrese el ID que desea dar de baja: '))
        
        if ID in productos: 
            productos.pop(ID)
            
        else: 
            return False 
        
        
    elif opc=='M':
        print(productos)
        v=0
        while v==0:
            try: 
            
                que=int(input('Ingrese el ID que desea modificar: '))
                v=1 
            except ValueError: 
                
                print('Ingrese un numero entero')
                
                
            if que in productos:
                p=0
                while p==0:
                    
                    try: 
                        precio=float(input('Ingrese el precio: '))
                        
                    except ValueError: 
                        print('Ingrese un valor!!')
                        
                    else: 
                        
                        if precio>0:
                            
                            productos[que][1]=precio 
                            p=1
                        else: 
                            print(f'Ingrese el precio de {productos[que]} mayor a 0!')
                
                return True 
            
            else: 
                return False
                
        

                    
    
    if opc=='ABC':
    
        return True
    
    else: 
        
        return False 
    





b=0
while b==0:
    
    print(''' menu
          1) Carga de una venta
    2) Lista, Alta (agregar o nuevo), B (Baja o borrar) o M (modificacion) de los productos
    3) Total de ventas
    f o F) Finaliza el programa''')
    
    op=menu()
    
    if op=='1':
        k=vender(productos)
        print(k)
        
    elif op=='2':
        labm(productos)
        
    elif op=='3':
        print('total de ventas')
    
    elif op=='f':
        print('Saliendo del programa')
        print(' ')
        b=1 
        
    else: 
        print('Opcion no valida ')
    