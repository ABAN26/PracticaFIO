pacientes={}

def menu():
    print('''---Menu----
    1) Carga
    2) Busqueda
    3) Listar IMC
    f o F) Finalizar''')
    
    opc=input('Ingrese una opcion: ').lower()
    
    return opc 


def carga():
    
    b=0
    
    while b==0:
       
        nombre=input('Ingrese el nombre del paciente: ')
        
        apellido=input('Ingrese el apellido del paciente: ')
        
        clave= nombre+ ' '+apellido 

        if clave in pacientes: 
            
            print('El paciente ya se encuentra cargado. Reintente.')
            
        else: 
            
            lista=[]
            c=0 
           
            while c==0:
                
                altura=float(input(f'Ingrese la altura de {clave} en metros: '))
                
                if altura<0:
                    b=1
                    c=1
                    print('Carga Terminada.')
                
                elif altura>=1 and altura<=2.10:
                    c=1
                    
                    lista.append(altura)
                    
                    c1=0 
                    while c1==0:
                        
                        peso=float(input('Ingrese el peso del paciente: '))
                        
                        if peso>=30 and peso<=200:
                            c1=1 
                            
                            lista.append(peso)
                        else: 
                            print('Ingrese un peso valido (entre [30-200])')


                    c2=0
                    while c2==0:
                        
                        edad=int(input('Ingrese la edad: '))
                        
                        
                        if edad>=10 and edad<=100:
                            
                            c2=1
                            lista.append(edad)

                        else: 
                            print('Igrese una edad valida. [10-100] ')
                            
                    alturaenCm=altura*100
                    
                    peso_recomendado=((alturaenCm-100)+(edad*0.1))*0.9
                
                    lista.append(peso_recomendado)
                    
                    pacientes[clave]=lista 
                           
                
                else: 
                    print('Ingrese una altura entre [1-2.10]')
                    
           
                    

    print(pacientes)
    
    return True 
    
def rango_peso(n1,n2):
    
    for i in pacientes: 
        
        dicc={}
        lista=[]
        
        
        if (pacientes[i][1]>=n1) and (pacientes[i][1]<=n2):
            
            nombre=i
            peso=pacientes[i][2]
            edad=pacientes[i][1]

            lista.append(peso)
            lista.append(edad)
            
            dicc[nombre]=lista
            
            print(dicc)

        else: 
        
            return False 
    





valid1=False 
b=0
while b==0:
    
    op=menu()
    
    if op=='1':
        
        valid1=carga()
        
    elif op=='2' and valid1==False:
        
        print('No hay datos para mostrar')
        
    elif op=='2' and valid1==True:
        
        c=0
        
        while c==0:
            try: 
                a=float(input('Ingrese un numero: '))
                
                b=float(input('Ingrese otro numero: '))

            except ValueError: 
                
                print('intente con un numero')
                
            else: 
                
                if a>=30 and b>a and b<=200:
                    
                    val2=rango_peso(a, b)
                    
                    c=1 
                    
                    print(val2)
                    
                    if val2==False: 
                        
                        print('NO existen personas en ese rango')

                else: 
                    
                    print('reintente ingresando un intervalo cerrado con valores validos')
                
                
    elif op=='3':
        print('listar IMC')
        
    elif op=='f':
        print('Saliendo del programa!')
        b=1
        
        
    else: 
        print('Opcion NO valida! Reintente')
        print('''
              
              ''')