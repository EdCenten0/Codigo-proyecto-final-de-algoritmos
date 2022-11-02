# Traduccion de pseint 

if __name__ == '__main__':
	# Se definen las variables a utilizar
	num = 0
	aux = 0
	j = 0
	i = 0
	c = 0
	datos = 0

	# Se pide al usuario ingresar la cantidad de datos,    
	print("Ingrese la cantidad de datos que se van a ordenar: ")
	num = int(input())
	# se declara un arreglo de num elementos
    
	datos = [int() for ind0 in range(num)]
	# se leen uno por uno los num* datos y se los guarda en el arreglo(vector)

	for i in range(num):
		print("Ingrese el dato ",i+1,":")
		datos[i] = int(input())
	# Se inicia la comparacion desde la posicion 1 hasta la posicion num del vector

	for i in range(num):
		# La primera comparacion arranca en la posicion 2 del vector
		for j in range(i+1,num):
			# Si datos[1] es mayor que datos[2] entonces
			if (datos[i]>datos[j]):
				# guarde en la variable aux el valor contenido en el vector datos[j]
				aux = datos[i]
				# Coloque el valor que existe en el vector[j] dentro del vector[i]
				datos[i] = datos[j]
				# Ahora lo que estaba en el vector[i] lo colocamos dentro del vector[j]
				datos[j] = aux
				# Termina primera comparacion

			# Termina el primer ciclo y suma 1 a j, para continuar con la tercera posicion y sucesivamente hasta llegar al valor de num

		# cuando J en el primer ciclo alcanza el valor de num arranca una nueva comparacion de datos{i+1] en donde j toma nuevamente el valor de i+1
		# I se repite uno a uno hasta alcanzar el valor de num
	print("*****************************************************")
	for c in range(num):
		print("El orden logico segun QUICKSORT es ",datos[c])