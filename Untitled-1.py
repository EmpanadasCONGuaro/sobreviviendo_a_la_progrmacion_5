x = float(input("ingrese la cordenada en x del centro del circulo: "))
y = float(input("ingrese la cordenada en y del centro del circulo: "))
r = float(input("ingrese el radio del circulo: "))

w = float(input("ingrese la coordena en x del punto: "))
z = float(input("ingrese la coordena en y del punto: "))

a = ((w - x) ** 2)
b = ((z - y) ** 2)
c = ((a + b) ** 0.5)

if c < r or c == r:
  print("la coordenada",w, "," ,z, "pertenece a la circunferencia")
else:
  print ("la coordenada no pertenece a la circuferencia")