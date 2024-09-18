# Code by: Roberto Ochoa Cuevas

# Imports
import math

# Mensajes de inicio
print('**Bienvenido al calculo de desviacion media**');
print('Para comenzar ingrese los datos (x)');

# Establecer variables
datos = [];

# Loop de pedir datos
while(True):
    datosCrudos = input('Ingrese el dato numerico (ingrese n para salir): ');
    if(datosCrudos == 'n' ):
        break;
    datos.append(float(datosCrudos));

# Sacar la media
media = sum(datos) / len(datos);
print(f'La media es: {media}');

# Sacar la desviacion estandar de cada elemento (x - media)
desviacion = [];
for dato in datos:
    desviacion.append((dato - media));

print(f'\n')
print(f'Lista de datos: {datos}')
print(f'Desviaciones: {desviacion}')

# Sacar la el cuadrado de cada desviacion

cuadrados = [];
for desv in desviacion:
    cuadrados.append(pow(desv,2));
print('\n')
print(f'los cuadrados son:  {cuadrados}');

# sacar la variabilidad (s^2) dividiendo la sumatoria de los cuadrados sobre n-1
variabilidad = sum(cuadrados) / (len(datos) - 1);
print(f'La variabilidad es de {variabilidad}')

# Sacar la desvicacion de la media sacando la raiz de la variabilidad
desviacionDeLaMedia = math.sqrt(variabilidad);
print(f'La desviacion de la media es: {desviacionDeLaMedia}');