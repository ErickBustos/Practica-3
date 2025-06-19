# Muestra un mensaje para indicar el tipo de conversión
print("Indique si es binario o decimal")
conversor = input()  # Guarda la respuesta, puede ser 'binario' o 'decimal')

## BINARIO A DECIMAL ----------------------------------------------------
if conversor.lower == "binario":  
    print("Si es binario")
    print("Dame el número binario (8 dígitos): ")
    numero = list(input())  # Convierte el número binario ingresado como string a una lista de caracteres

    x = [128, 64, 32, 16, 8, 4, 2, 1]  # Representa el peso de cada bit de izquierda a derecha
    sumadores = []  # Lista para guardar los valores que sumarán al total decimal

    for i in range(0, len(x)):  # Recorre los 8 bits
        if numero[i] == "1":  # Si el bit es '1'
            sumadores.append(x[i])  # Agrega el peso correspondiente a la lista de sumadores

    print("Valor en decimal: ", sum(sumadores))  # Suma los valores y muestra el resultado en decimal

## DECIMAL A BINARIO ----------------------------------------------------
if conversor.lower() == "decimal":  
    print("Ingrese valor decimal 0-255: ")
    valor = int(input())  # Convierte el valor ingresado a número entero
    print("El valor ingresado es: ", valor, "tipo", type(valor))  # Muestra el valor y su tipo de dato

    x = [128, 64, 32, 16, 8, 4, 2, 1]  # Lista con los valores binarios de cada posición
    binario = [0, 0, 0, 0, 0, 0, 0, 0]  # Lista para guardar los bits resultantes (inicialmente todo en 0)

    for e in range(0, len(x)):  # Recorre cada valor binario desde el más grande al más pequeño
        if valor >= x[e]:  # Si el valor es mayor o igual al peso actual
            binario[e] = 1  # Coloca un 1 en esa posición
            valor = valor - x[e]  # Resta el valor correspondiente

    print("El valor decimal a binario es: ", binario)  # Muestra la lista binaria final
