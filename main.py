# seleccionar si quiere calcular años enteros o con decimales
print(
    "Bienvenido a la calculadora de años. Podrá saber a cuantos segundos equivale la cantidad de años que desee, ya sean enteros o con decimales."
)

año = input("Ingrese la cantidad de años que quiere pasar a segundos: ")
# detectar que quiere calcular el usuario
try:
  valor = int(año)
  if valor == 4:
    print("El valor ingresado es un año bisiesto")
    print((valor * 31622400) / 4)
  else:
    print((valor * 31536000) / 1)
except ValueError:
  try:
    valor = float(año)
    # print("es un decimal")
    # calculo
    print((valor * 31536000) / 1)
  except ValueError:
    print("No es un número")

# en 1 año hay 31.536.000 segundos
# en 1 dia hay 86400 segundos
# en 1 año bisiesto hay 31.622.400 segundos
# print((año * 31536000) / 1)
