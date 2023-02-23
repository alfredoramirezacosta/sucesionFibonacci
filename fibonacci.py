n = int(input("Ingrese la cantidad de numeros a imprimir de la sucesion de Fibonacci: "))
# Definir los primeros dos términos de la serie
n1, n2 = 0, 1
count = 0
# Validamos que sea un numero mayor que cero
while n <= 0:
   n = int(input("Ingrese un número entero: "))
#Imprimira la sucecion hasta llegar a la cantidad de numeros ingresada
print("Sucesion de Fibonacci:", end=" ")
while count < n:
    print(n1, end=" ")
    n3 = n1 + n2
    # Actualizamos los valores
    n1 = n2
    n2 = n3
    count += 1