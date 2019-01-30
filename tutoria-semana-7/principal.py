# se importa los paquetes necesarios
from modelo.modelado import *
from data.archivo import *
from combinacion.combinacion import *

m = MiArchivo() # se crea un objeto

lista = m.obtener_informacion() # se le agrega la informacion a la lista

lista = [l.split(";") for l in lista] # se divide la lista con el split

# se crea dos listas vacias
lista_edades = [] 

print("Informacion completa\n") # encabezado
for d in lista:# se recorre la lista
	j = Persona(d[0],d[1],d[2]) # se crea un objeto dandole los parametros de la lista
	print(j) # se imprime el objeto
	lista_edades.append(j.getEdad()) # se toma la edad y se la agrega a la lista edades

print("\nLista de edades:") # encabezado
print(lista_edades) # se imprime la lista en desorden

merge_sort_result = merge_sort(lista_edades)   # se llama el metodo para ordenar 
print("\nEdades ordenadas") # encabezado
print(merge_sort_result,"\n") # sde imprime la lista ordenada

