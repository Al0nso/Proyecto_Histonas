"""Universidad Nacional Autónoma de México
@Autora: Gisselle Ibarra Moreno
Ciencias de la Computación, 8vo semestre
@Autora: Dulce María Montero
Biología, 8vo semestre
@Autora: Mariana Jocelyn Robles Lara 
Biología, 8vo semestre
@Autor: Medina Amayo D. Alonso 
Ciencias de la Computación, 8vo semestre
Lenguaje: Python
Versión del Lenguaje: Python 3
Versión del programa: v1.0
Fecha: 07/JUN/2022
El comando para correr el programa:
python3 comparadorHistonas.py
"""
#No se en que semestre van, perdón
#Saqué sus nombres del classroom, no soy tan stalker

"""Método para crear un arreglo de String con las secuencias
La secuencia 0 es la canónica
La ruta por default es al archivo del 07/06/2022
Recibe la ruta al documento en forma de String
Devuelve una lista de String"""
def obten_secuencias(ruta="clustalo-I20220608-002558-0612-33983684-p1m.clustal_num"):
    secuencias = [""]*18 #Lista de las secuencias, tenemos 20
    numero_secuencia = 0 #Secuencia en la que vamos

    f = open(ruta, "r") #Abrimos el archivo en forma de lectura
    linea = f.readline() #Leemos la primera línea

    while linea: #Leeremos todo el archivo

        while(not "H3_HOMO_SAPIENS" in linea): #Buscamos el comienzo de las secuencias
            linea = f.readline()

        while(not "*:" in linea): #Leemos hasta el final del bloque
            i = 29 #Donde comienzan las secuencias
            while(not linea[i] == "\t"):#Al llegar al final
                secuencias[numero_secuencia] += linea[i]
                i+=1#Agregamos toda la secuencia en la lista de uno en uno
            linea = f.readline()
            numero_secuencia += 1 #Pasamos a la siguiente secuencia del mismo bloque
        numero_secuencia = 0 #Como son los mismosorganismos los guardaremos juntos
        linea = f.readline() #Si existe, el while lo detecta y sigue leyendo, si no es el eof
    f.close()
    return secuencias


"""Método para comparar un par de histonas
Recibe la histona canónica y la secuencia del organismo a comparar
Devuelve el porcentaje de la diferencia de la canónica con la del organismo, -1 si son de longitud diferente"""
#Ejemplo
#Canónica: MGPRR
#Organismo: MGPRG
#compara_histonas(canonica, organismo) = 20
def compara_histonas(canonica, organismo):
    total_pares_de_bases = len(canonica) #Total de pares de bases en la secuencia canónica
    total_diferencias = 0 #Total de diferencias con la secuencia del organismo
    if(len(organismo) != len(canonica)):
        return -1
    for i in range(total_pares_de_bases):
        total_diferencias += 1 if(  canonica[i]!=organismo[i] ) else 0
    return (total_diferencias*100)/total_pares_de_bases


"""Método que compara a todas las secuencias con la canónica
Recibe una lista de secuencias con la canónica al inicio
Devuelve una lista con valores que significan el porcentaje de diferencia"""
def obtenerComparaciones(secuencias):
    comparaciones = [0]*len(secuencias)
    for i in range(len(secuencias)):
        comparaciones[i] = compara_histonas(secuencias[0],secuencias[i])
    return comparaciones