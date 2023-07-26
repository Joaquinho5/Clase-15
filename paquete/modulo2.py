def ano_bisiesto(anio):
  if anio % 4 == 0 and (anio % 400 == 0 or anio % 100 != 0):
    print("El año es bisiesto")
  elif type(anio) != int:
    print("Por favor, ingresa un número válido.")
  else:
    print("El año no es bisiesto")

def area_rectangulo(base, altura):
  cuenta = base*altura
  return cuenta

def area_circulo(radio):
  cuenta = (radio**2) * 3.14159
  return cuenta

def relacion(num1, num2):
  if num1 > num2:
    return 1
  elif num2 > num1:
    return -1
  elif num1 == num2:
    return 0

def intermedio(num1, num2):
  cuenta = (num1 + num2) / 2
  return cuenta

def recortar(num1, lim1, lim2):
  if num1 < lim1:
    return lim1
  elif num1 > lim2:
    return lim2
  elif num1 >= lim1 and num1 <= lim2:
    return num1

def separar(lista):
  pares = []
  impares = []
  for n in lista:
    if n%2==0:
      pares.append(n)
    else:
      impares.append(n)

  print(pares)
  print(impares)