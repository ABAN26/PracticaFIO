dicc={}

def carga(N):
    
    for i in range(1,N+1):
        lista=[]
        c=0
        while c==0:
            
            apellido=input("Ingrese el apellido del empleado: ").capitalize()
         
            nombre=input("Ingrese el nombre del empleado: ".capitalize())
            
            completo=apellido+" "+nombre 
            
            if completo in dicc: 
                
                print("El empleado ya se encuentra cargado")
                
                print("Ingrese otro empleado")

                print(" ")

            else: 
                c=1 
                
                
                
                c1=0
                
                while c1==0:
                    
                    try: 
                        edad=int(input(f"Ingrese la edad del {i} empleado:  "))
                        
                    except ValueError: 
                         
                        print("Ingrese la edad en forma de numero")
                        
                    else: 
                        
                        if edad>0:
                            c1=1 
                            lista.append(edad)
                            
                c2=0
                while c2==0:
                  
                  sexo=input(f"Ingrese el sexo de {completo}: ").upper()
                  
                  if sexo=="F" or sexo=="M":
                      
                      lista.append(sexo)
                      c2=1
                      
                else: 
                    print("Ingrese (F)o (M) ")
                
                
                c3=0
                while c3==0:
        
                    try: 
                        antiguo=int(input(f"Ingrese la antiguedad de {completo}: "))
        
                    except ValueError: 
                                                
                          print("Ingrese la antiguedad del empleado en numeros")
                          
                    else: 
                        
                        if antiguo>0:
                            
                            c3=1 
                            lista.append(antiguo)
                            
                        else: 
                            print("La antiguedad debe ser un numero positivo")
                            
                c4=0
                while c4==0:
                    
                    try: 
                        sueldo=float(input("Ingrese el sueldo: "))
                        
                    except ValueError: 
                        print("Ingrese un sueldo real!")
                        
                    else: 
                        
                        if sueldo>0:
                            
                            c4=1 
                            lista.append(sueldo)
                        else: 
                            print("Ingrese un sueldo positivo")
                            
                    
                
        dicc[completo]=lista 
        print(dicc)
        
    return True 
            
def cantidad():
    contF=0
    contM=0
    for i in dicc: 
        if dicc[i][1]=="F":                
            contF+=1 
            
        else: 
            contM+=1 

    return [contM,contF]


def promedio():
    cont=0
    acu=0
    
    for i in dicc: 
        
        cont+=1
        acu+=dicc[i][3]
    
    prom=acu/cont

    
    return prom 



def buscar(arg):
    
    edadMinima=1000
    
    if arg=="MUJER": 
        
        arg="F"
        
        for i in dicc:
             
            if dicc[i][1]==arg:
                    
                 edadMinima=dicc[i][0]
                 
                    
                 if edadMinima>dicc[i][0]:
                
                    edadMinima=dicc[i][0]
                    
                    persona=dicc[i]
                    
    return persona
    





val=False 
b=0
while b==0:
    
    print(""" Menú
    1) Carga datos de N empleados
    2) Mostrar la cantidad de hombres y mujeres
    3) Mostrar el promedio de sueldo
    4) Buscar el empleado más jóven por sexo 
    f o F) Finalizar""")
    
    op=input("Ingrese una opcion: ").lower()
    
    
    if op=="1":
        c=0
        while c==0:
            try: 
                num=int(input("Ingrese un numero: "))
                
            except ValueError: 
                print("Ingrese un numero entero!")
                
            else: 
                
                if num>0:
                    c=1 
        
                    val=carga(num)
                else: 
                    print("Ingrese un valor positivo!!")
    elif op=="2" and val==True:
        
        cantidad()
        
        print("La cantidad de hombres y mujeres se presenta en la sigueinte lista: ")
        print(cantidad())
        
    elif op=="3" and val==True:
        
        muestro=promedio()
        
        print(f"El promedio de los sueldos es: {muestro}")
    
        
    elif op=="4" and val==True:
        
        z=0
        while z==0:
            busco=input("Ingrese ´Hombre´ o ´Mujer´ para buscar: ").upper()
            
            if busco=="HOMBRE" or busco=="MUJER":
                z=1 
                
        
                joven=buscar(busco)
                
                print("El empleado más joven es: {joven}")
                
       
            else: 
                print("""Ingrese un género válido para buscar en el diccionario! 
                      
                      """)
    elif op=="f":
        print("Saliendo del programa")
        b=1
        
    else: 
        print("""Ingrese una opción válida 
              
              """)