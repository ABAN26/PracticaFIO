alumnos={}

def menu():
    print('''---Menu--
          1) Cargar alumnos
    2) Cargar notas de parciales 
    3) Ver datos 
    S o s) Salir''')
    
    opc=input('Ingrese una opcion: ').lower()
    
    return opc 

def carga(N):
    
    for i in range(N):
    
        dicc={}
        
        b1=0 
        
        while b1==0:
            
            Nlegajo=input('Ingrese el numero de legajo del alumno: ')
            
            if Nlegajo in alumnos: 
                
                print('El alumno se encuentra cargado.')
                
            else: 
                b1=1
                
                nombre=input(f'Ingrese el nombre de {Nlegajo}: ')
                apellido=input(f'Ingrese el apellido de {Nlegajo}: ')

                dicc['nombre']=nombre
                dicc['apellido']=apellido 
                
                alumnos[Nlegajo]=dicc
                
                if alumnos[Nlegajo]['apellido']>='A' and alumnos[Nlegajo]['apellido']<='N':
                    
                    dicc['comision']=1
                
                else: 
                    
                    dicc['comision']=2 
                
                 
    return True  
            
def cargarNotas():
    
    for j in alumnos: 
        
        lista=[]
        
        b=0
        
        while b==0:
            a=alumnos[j]['nombre']
            
            nota1=float(input(f'Ingrese la primer nota de {a}: '))
        
            if nota1>=0 and nota1<=10:
                
                lista.append(nota1)
                b=1 
                
            else: 
                print('Ingrese una nota valida')

        b1=0
        
        while b1==0:
            nota2=float(input('Ingrese la nota 2 : '))
            
            if nota2>=0 and nota2<=10:
                
                lista.append(nota2)
                b1=1 
                
            else: 
                print('Reingrese la nota del segundo parcial ')
                
                
        
        
            alumnos[j]['notas']=lista

            
        prom=(nota1+nota2)/2
        
        if nota1>=6 and nota2>=6 and prom>=7:
            condicion='Regular'
        else: 
            condicion='Libre'
        
        alumnos[j]['condicion']=condicion
        
    return True 

def verdatos(alumnos, elec):
    cont=0
    
    
    if elec=='C':
        for i in alumnos: 
            print(i, ": ", alumnos[i])
        
    elif elec=='R':
        
        cantidad=len(alumnos)
        
        for i in alumnos:
            
            if alumnos[i]['condicion']=='Regular':
                cont+=1 
    
        print(f'''la cantidad de alumnos en total es: {cantidad}
          El cantidad total de aprobados es: {cont}''')
          
          
            
    
    

        



val=False
val2=False
b=0
while b==0:
    
    op=menu()
    
    if op=='1':
        c=0
        while c==0:
            try: 
                num=int(input('Ingrese la cantidad de notas que desea cargar: '))
                
            except ValueError: 
                print('Ingrese un numero entero')
                
            else: 
                
                if num>0:
                    val=carga(num)
                    c=1 
                    
                else: 
                    print('Ingrese un numero mayor a cero')
                    
                    
        
    
    elif op=='2' and val==True:
        
        val2=cargarNotas()
        
        
        
    elif op=='3' and val2==True:
        
        q=0
        while q==0:
            
            ver=input('Ingrese "R" si desea ver la version Resumida o "C" para ver la version completa: ').upper()
            
            if ver=='R' or ver=='C':
                
                verdatos(alumnos, ver)
                
                q=1
    
            else: 
                print('''OPCION INCORRECTA
                      REINTENTE''')
            
            
        
        print('ver datos')
        
    elif op=='s':
        print('''Saliendo del programa
              
              ''')
        b=1
    else: 
        print('OPCION INCORRECTA')