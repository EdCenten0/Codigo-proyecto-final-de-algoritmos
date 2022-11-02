def ordenar():
    #Se crea una lista
    arr = [ 40, 8, 5, 20, 1]

    #El primer ciclo itera desde el principio hasta el final 
    for i in range(len(arr)): 
        #El segundo ciclo itera desde el principio hasta el tamaño del arreglo, -i, -1
        #'-i', indica el numero de elementos que estan en la pos final
        for j in range(len(arr) - i - 1):
            #Se comparan los elementos por pareja. j indica el primer elemnto de las parejas
            #[j+1] indica el elemento de la derecha. 
            if arr[j] > arr[j+1]: #arr[j] llega hasta el penultimo elemento y lo compara con el siguiente
                #si la condicion anterior se cumple, se hace un intercambio entre los valores
                temp = arr[j] 
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
        
    print(arr)

ordenar()