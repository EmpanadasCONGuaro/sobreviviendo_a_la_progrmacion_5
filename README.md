# sobreviviendo_a_la_progrmacion_5

# 1. Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.



- DIAGRAMA DE FLUJO  PUNTO 1


![image](https://github.com/EmpanadasCONGuaro/sobreviviendo_a_la_progrmacion_5/assets/142174506/a77ee1ba-0688-421b-a94c-b0f3268279be)

  


# 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.


```pseudocode
i:int=0
print("lista de impares")
while i <= 999:
    i=i+1
    if i % 2  == 0:
      continue
    print(i)
    

print("lista de pares")
i:int=0
while i <= 1000:
    i=i+1
    if i % 2 != 0:
      continue
    print(i)
    

```

- DIAGRAMA DE FLUJO 2
  

![image](https://github.com/EmpanadasCONGuaro/sobreviviendo_a_la_progrmacion_5/assets/142174506/62061f60-1c05-424a-9c55-e42e08b37eeb)




# 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado



```pseudocode
i: int= 0
i: int= int(input("ingrese un numero:"))
print(i)
while i >= 2:
    i -= 1
    if i%2 !=0:
        continue
    print(i)

```


- DIAGRAMA DE FLUJO 3
  


![image](https://github.com/EmpanadasCONGuaro/sobreviviendo_a_la_progrmacion_5/assets/142174506/dcf3d087-fdfc-4802-aa25-bfdee6f63ab9)




# 4. En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.



```pseudocode
A: int = 25000000
TasaDeCrecimeintoA:float=0.02
B: int = 18500000
TasaDeCrecimeintoB:float=0.03
Año: int= 2022

while B <= A:
    A= A*(1+ TasaDeCrecimeintoA)
    B= B*(1+ TasaDeCrecimeintoB)
    Año += 1
print("el año en el que el pais B supera al pais A es " +str(Año))

```


# 5. Imprimir el factorial de un número natural n dado.



```pseudocode
n = int(input("ingrese un numero:"))
factorial = 1
while 0 < n:
  factorial *= n
  n -= 1

print("El factorial es "  +str(factorial))
```



# 6. Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.



```pseudocode
import random 
NumeroMenor = 1
NumeroMayor = 100
bandera : bool = True
while bandera == True:
  NumeroRandom=random.randint(NumeroMenor, NumeroMayor)
  Adivinanza = input("El número es mayor, menor, o igual que: " + str(NumeroRandom) + " ")
  if Adivinanza == "mayor":
    NumeroMenor = NumeroRandom + 1
  elif Adivinanza =="menor":
    NumeroMayor = NumeroRandom - 1
  else:
    break
print("El número es: " + str(NumeroRandom))  

```



# 7. Implementar un programa que ingrese un número de 2 a 50 y muestre sus divisores.



```pseudocode
x= int(input("ingrese un numero entre 2 y 50:"))

if 50 >= x >= 2:
    print("los divisores enteros de " +str(x)+ " son:")
    y=1
    while y <= x:
        if x%y==0:
            print(y)
        y += 1

```


# 8. 



