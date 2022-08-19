
import csv

e_encontrados=[]
elementos_encontrados = []
ordenados_rutas=[]
lista_rutas =[]
lista_rutas_cantidad= []
suma=0
dicc_transportes_suma = {}

with open ("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)

    #Se crea una sublista con todos los origenes y destinos (rutas)
    for elementos in lector:    
        if not elementos in elementos_encontrados:
              # Elementos_encontrados acumula los dic que ya se analizaron para no repetirlos
              elementos_encontrados.append(elementos)
              # Se cuentan los elementos
              contar_elementos = elementos_encontrados.count(elementos)
              # Si hay mas de 1 repeticion, crear el diccionario nuevo
              if contar_elementos >= 1:
                nuevo_elemento = {}
                nuevo_elemento['origin'] = elementos['origin']
                nuevo_elemento['destination'] = elementos['destination']
                nuevo_elemento['cantidad'] = contar_elementos 
                lista_rutas.append(nuevo_elemento)
    
    #Se lleva a cabo la iteración de la sublista para contabilizar la demanda, en base al mayor número de repeticiones (apariciones), tanto para importación como exportación
    for e in lista_rutas:    
        if not e in e_encontrados:
              # Elementos_encontrados acumula los dic que ya se analizaron para no repetirlos
              e_encontrados.append(e)
              # Se cuentan los elementos
              contar_elementos = lista_rutas.count(e)
              # Si hay mas de 1 repeticion, crear el diccionario nuevo
              if contar_elementos >= 1:
                nuevo_elemento = {}
                nuevo_elemento['origin'] = e['origin']
                nuevo_elemento['destination'] = e['destination']
                nuevo_elemento['cantidad'] = contar_elementos 
                lista_rutas_cantidad.append(nuevo_elemento)
   
   
    #Srive para orenar las 10 rutas más demandadas          
    for elementos in lista_rutas_cantidad:
        ordenados_rutas = sorted(lista_rutas_cantidad, key=lambda lista_rutas_cantidad: int(lista_rutas_cantidad["cantidad"]), reverse=True)
    #CAMBIARRRRRR A 10, DEBEN SER LAS DIEZZZZZZZZ RUTAS NY NO 2 DOS 
#CAMBIAR
#CAMBIAR
#CAMBIAR 2 POR 10   
    print(ordenados_rutas[:10])



with open ("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)

    
    #Se lleva a cabo la iteración para concoer los 3 medios de transportes más demandados
    for i in lector:
        if dicc_transportes_suma.get(i['transport_mode']) != None:
            suma += int(i['total_value'])
            dicc_transportes_suma[i['transport_mode']] = suma
        else:
            suma += int(i['total_value'])
            dicc_transportes_suma[i['transport_mode']] = suma         

print(dicc_transportes_suma)   



with open ("synergy_logistics_database.csv","r") as archivo_csv:
    lector = csv.DictReader(archivo_csv)

    suma=0
    dicc_transportes_suma = []
    #Obtener el número total de importaciones y exportaciones
    for i in lector:
        dicc_transportes_suma.append(i["total_value"])
    for x in dicc_transportes_suma:
        suma += int(x)
    print ("Total importaciones/exportaciones: ",suma)
       
