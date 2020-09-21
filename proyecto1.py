#Universidad del Valle de Guatemala
#Fisica 3 Proyecto 1
#Graficador de trayectoria de una particula
#Bryann Alfaro 
#Diego de Jesus Arredondo

#Importacion de librerias
import matplotlib.pyplot as pyplot
import math as math
import numpy

k=input("Press to start...")
#Masas de particulas
masas = [1.67E-27 , 9.1E-31 , 9.11E-31 , 6.64E-27, 1.9E-28, 1.67E-27, 3.34E-27, 3.2E-27, 1.9E-28, 3.2E-27]

#Cargas de particulas
cargas = [1.6E-19,  -1.6E-19, 1.6E10-19, 3.21E-19, -1.6E-19, 0.0, 1.6E-19, -1.6E-19, 1.6E-19, 1.6E-19]
coordenadasX = []
coordenadasY = []


print("**********TRAYECTORIA DE UNA PARTICULA****************")
print("1. Proton ") 
print("2. Electron")
print("3. Positron")
print("4. Alfa")
print("5. Muon")
print("6. Neutron")
print("7. Nucleo de Deuterio")
print("8. Tauon")
print("9. Antimuon")
print("10. Antitauon")
print("****************************************************")

#Peticion de datos
particula = int(input("Ingrese la opcion de la particula que desea evaluar [1-10]: "))
velocidad= float(input("Ingrese la velocidad inicial en m/s: "))
velAngulo = float(input("Ingrese el angulo de la trayectoria en grados [0-90]: "))
campoElectrico= float(input("Ingrese la magnitud del campo con signo: "))

#aceleracion = carga*campo/masa
aceleracion = (cargas[particula-1]*campoElectrico)/masas[particula-1]
print("Aceleracion: ",aceleracion)
if(aceleracion==0):
  #velocidad coordenada x=  v*cos thetha
  velocidadx = velocidad*math.cos(velAngulo/180)
  print (velocidadx)

  #velocidad coordenada y= v*sin thetha
  velocidady = velocidad*math.sin(velAngulo/180)
  print (velocidady)

  tiempoSubida = 0 #Tiempo en que llega al tope
  tiempoTotal = tiempoSubida*2
  print("Tiempo de subida: ",tiempoSubida)
  print("Tiempo total del recorrido:",tiempoTotal)

  for t in numpy.arange(0, 5):
    coordenadaX = velocidadx*t #Cuanto recorrio
    coordenadaY = 0
    coordenadasX.append(coordenadaX)
    coordenadasY.append(coordenadaY)

  pyplot.plot(coordenadasX, coordenadasY)
  pyplot.ylabel("Y position")
  pyplot.xlabel("X position")
  pyplot.title('Movement of particle')
  pyplot.show()

else:
  #velocidad coordenada x=  v*cos thetha
  velocidadx = velocidad*math.cos(velAngulo/180)
  print (velocidadx)

  #velocidad coordenada y= v*sin thetha
  velocidady = velocidad*math.sin(velAngulo/180)
  print (velocidady)

  tiempoSubida = velocidady/aceleracion #Tiempo en que llega al tope
  tiempoTotal = tiempoSubida*2
  print("Tiempo de subida: ",tiempoSubida)
  print("Tiempo total del recorrido:",tiempoTotal)

  for t in numpy.arange(0, tiempoTotal, tiempoTotal/20):
    coordenadaX = velocidadx*t #Cuanto recorrio
    coordenadaY = velocidady*t - ((aceleracion * t**2)/2)
    coordenadasX.append(coordenadaX)
    coordenadasY.append(coordenadaY)

  pyplot.plot(coordenadasX, coordenadasY)
  pyplot.ylabel("Y position")
  pyplot.title('Movement of particle')
  pyplot.xlabel("X position")
  pyplot.show()
  k=input("Press to finish..")