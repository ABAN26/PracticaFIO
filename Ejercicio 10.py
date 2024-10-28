agenda={}
grupos=['Trabajo']


def menu():
    
    print('''---- Menu----
    1) Agregar contacto
    2) Buscar contacto
    3) Alta de grupos
    4) Mostrar grupos''')
    
    opc=input('Ingrese una opcion: ').lower()
    
    if opc in '1234s':
    
        return opc 
    

def agregar_contacto():
    
    nombre=input('Ingrese el nombre que desea agregar: ').capitalize()
    
    if nombre in agenda: 
        
        print('El nombre ya existe')
        print(' ')
        
        return menu()
    
    else: 
        
        lista=[]
        
        b=0
        while b==0:
            try: 
                
                tel=int(input(f'Ingrese el numero de telefono de {nombre}: '))
                
            except ValueError: 
                
                print('Error. Ingrese el numero sin puntos. ')
                
                
            else: 
                
                if tel>0:
                    b=1    
                    
                    lista.append(tel)
                    
                else: 
                    print('Ingrese un numero de telefono valido.')
    
        b1=0
        while b1==0:
            
            grupo=input(f'Ingrese el grupo al que pertenece {nombre}: ').capitalize()
            
            if grupo in grupos: 
                
                lista.append(grupo)
                b1=1 
                
            else: 
                print('Ingrese el grupo al que pertenece que se encuentra en la lista de grupos! ')
                
                print(grupos)
        
        agenda[nombre]=lista
        
        return True 

def buscar_contacto(name):

    if name in agenda: 
        print(name, ':', agenda[name])
        
    else: 
        print('No hay concidencias')

def cargar_grupos():
    
    c=1
    while c==1:
        
        nombre_grupo=input('Ingrese el nombre que desea cargar: ')
        
        if nombre_grupo in agenda: 
             
            print(f'Ya existe {nombre_grupo} en la agenda')
            print('''
                  
                  Reintente''')
                  
        else: 
            c=0
            
            grupos.append(nombre_grupo)
            
            
            
        

def buscar_grupo():
    
    lista=[]
    
    
    
    c=0
    while c==0:
        print(grupos)
        
        nombre_busca=input('Ingrese el nombre que desea buscar: ').capitalize()
       
        
        
        if nombre_busca not in grupos:
            
            print('Reingrese el nombre del grupo.')
            
             
        else: 
            c=1
            
            personas=[]
            
            for i in agenda: 
                
                if agenda[i][1]==nombre_busca:
                    nombre=i 
                    datos=agenda[i]
                    personas.append(nombre)
                    personas.append(datos)

            
            lista.append(personas)
    
    return lista                

            
                    
                    
                
                
                
            
    

val=False
b=0
while b==0:
    
    op=menu()
    
    if op=='1':
        
        val=agregar_contacto()

    elif op=='2' and val==True:
        
        n=input('Ingrese el nombre que desea buscar: ')
        
        buscar_contacto(n)
        
    elif op=='3':
        
        cargar_grupos()
        
        
    elif op=='4' and val==True:
        
        c=buscar_grupo()
        print(c)
        
        
    elif  op=='s':
        print('Saliendo del programa.')
        b=1
    else: 
        print('Ingrese una opcion valida')


