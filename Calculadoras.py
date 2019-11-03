print("CALCULADORA N°1")
#Calcularemos el volumen de una esfera

# declaracion de variables
pi,radioE=0.0,0.0

# asigancion de valores:
pi=3.14
radioE =8
# calculo:

volumen =4/3*pi*(radioE**3)

#mostrar valores
print("El valor de pi es:" + str(pi))
print("El valor del radio es:" + str(radioE))
print("El volumen de la esfera es:" + str(volumen))

print("CALCULADORA N°2")
#Calcular el volumen de un cilindro

# declaracion de variables
pi,radioC,altura=0.0,0.0,0.0
# asignacion de variables:
pi = 3.14
radioC = 10
altura = 20
#calcular
volumenC = pi*(radioC**2)*altura
#mostrar
print("El pi es:" + str(pi))
print("El radio de un cilindro es:" + str(radioC))
print("El resultado del volumen de un cilindro es:" + str(volumenC))

print("CALCULADORA N°3")
#Calcular el area de un circulo
#declaracion de variables
pi,radioCi,area=0.0,0.0,0.0
#asignacion de variables
pi= 3.14
radioCi = 10

#calcular
areaC = pi*(radioCi**2)
#mostrar valores
print("El pi es: " + str(pi))
print("El circulo es: " + str(radioCi))
print("El area de un circulo es: " + str(areaC))

print("CALCULADORA N°4")
#Calcular el area de un trapecio

#declaracion de variables
baseMayor,baseMenor,altura,area=0.0,0.0,0.0,0.0
#asignacion de variables
baseMayor = 20
baseMenor = 10
altura = 15
#calcular
area_trapecio = (baseMayor + baseMenor )/2*altura
#mostrar valores
print("La base mayor de un trapecio es: " + str(baseMayor))
print("La base menor de un trapecio es: " + str(baseMenor))
print("El resultado de un area de Trapecio es: " + str(area_trapecio))

print("CALCULADORA N°5")
#Hallar el área del paralelogramo a base de dos lados y el ángulo entre ellos

#declaracion de variables
lado1,lado2,sen30,area=0.0,0.0,0.0,0.0
#asigancion de valores
lado1 = 10
lado2 = 30
sen30 = 1/2
#calcular
area_paralelogramo = lado1*lado2*sen30
print("El lado 1 es: " + str(lado1))
print("El lado 2 es: " + str(lado2))
print("El seno de 30 es: " + str(sen30))
print("El resultado del area del paralelogramo es: " + str(area_paralelogramo))

print("CALCULADORA N°6")
#Hallar el area del rombo a base sus diagonales

#declaracion de variables
d1,d2,area=0.0,0.0,0.0
#asignacion de variables
d1 = 20
d2 = 30
#calcular
areaR = 1/2* d1*d2
#mostrar valores
print("EL diagonal 1 es: " + str(d1))
print("El diagonal 2 es: " + str(d2))
print("El area del rombo es: " + str(areaR))

print("CALCULADORA N°7")
#Calcular el perimetro de un triangulo

#declaracion de variables
ladoa,ladob,ladoc=0,0,0
#asignacion de variables
ladoa = 30
ladob = 20
ladoc = 50
#calcular
perimetro = ladoa + ladob + ladoc
#mostrar valores
print("El lado a es: " + str(ladoa))
print("El lado b es: " + str(ladob))
print("El lado c es: " + str(ladoc))
print("El perimetro de un triangulo es: " + str(perimetro))

print("CALCULADORA N°8")
#Calcular su  Tasa de natalidad
#declaracion de variables
numNac,pobTotal,tasaNatalidad=0,0,0
#asignacion de variables
numNac = 2545
pobTotal = 10459
#calcular
tasaNatalidad = (numNac/poTtotal)*100
#mostrar valores
print("El numero de personas nacidas es: " + str(numNac))
print("La poblacion total es: " + str(pobTotal))
print("La Tasa de Natalidad es: " + str(tasaNatalidad))

print("CALCULADORA N°9")
#Calcular su Tasa de mortalidad
#declaracion de variables
muerteProv,pobTotal = 0,0
#asignacion de variables
muerteProv = 840
pobTotal = 8420
#Calcular
tasaMortalidad = muerteProv/pobTotal * 100
#mostrar valores
print("Las muertes Provocadas es: " + str(muerteProv))
print("La poblacion Total es: " + str(pobTotal))
print("Su tasa de mortalidad es: " + str(pobTotal) + "%")

print("CALCULADORA N°10")
#Determinar el tiempo en que recorre el niño de su casa hacia el colegio
#declaracion de variables
velocidad,distancia=0,0
#asignacion de valores
velocidad = 20
distancia = 400
#calcular
tiempo = distancia / velocidad
#mostrar valores
print("La velocidad es: " + str(velocidad))
print("La distancia es: " + str(distancia))
print("El tiempo que recorre es: " + str(tiempo))

print("CALCULADORA N°11")
#En cuanto tiempo tardara un automovil en alcanzar una velocidad de 60 km/h si parte de repospo
# con una aceleracion de 20 km/h2
#declarar variable
Vf,Vo,a =0,0,0
#asignacion de valores
Vf = 60
Vo = 0
a = 20
#calcular
t = Vf / a

#mostrar valores
print("La velocidad inicial es: " + str(Vo))
print("La velocidad final es: " + str(Vf))
print("La aceleracion es: " + str(a))
print("El tiempo que tardara el automovil es: " + str(t))

print("CALCULADORA N°12 ")
#Halla el tiempo de alcance
#declarar
V1,V2,d= 0.0,0.0,0.0
#asignar
V1=20
V2=10
d = 10
#calcular
tiempoAlcance = d/(V1+V2)
#mostrar
print("La velocidad 1 es: " + str(V1))
print("La velocidad 2 es: " + str(V2))
print("La distancia es: " + str(d))
print("El tiempo de alcance es: " + str(tiempoAlcance))

print("CALCULADORA N°13 ")
#Hallar el Tiempo de encuentro
#declarar
Va,Vb,dE = 0.0,0.0,0.0
#asignar
Va=10
Vb=8
d=20
#calcular
tiempoEncuentro= d/(Va-Vb)
#motrar
print("La velocidad a es: " + str(Va))
print("La velocidad b es: " + str(Vb))
print("La distancia es: " + str(dE))
print("El tiempo de encuentro es: " + str(tiempoEncuentro))

print("CALCULADORA N°14 ")
#Hallar la densidad
#declarar
masa,velocidad=0.0,0.0
#asignar
masa=10
velocidad=5
#calcular
densidad = masas/velocidad
#mostrar
print("La masa es: " + str(masa))
print("La velocidad es: " + str(velocidad))
print("La densidad es: " + str(densidad))

print("CALCULADORA N°15 ")
#Hallar el trabajo
#declarar
masaA,aceleracion,distancia=0.0,0.0,0.0
#asignar
masaA=5
aceleracion=6
distancia=10
#calcular
fuerza=masaA*aceleracion
trabajo=fuerza*distancia
#mostrar
print("La masa es: " + str(masaA))
print("La aceleracion es: " + str(aceleracion))
print("La distancia es: " + str(distancia))
print("La fuerza es: " + str(fuerza))
print("El trabajo es: " + str(trabajo))

print("CALCULADORA N°16")
#La energia cinetica
#declarar
masaE,velocidadE=0,0
#asignar
masaE=10
velocidadE=5
#calcular
Ec= (masa*(velocidadE**2))/2
#mostrar
print("La masa de la energia es: " + str(masaE))
print("La velocidad de la energia es: " + str(velocidadE))
print("La energia cinetica es: " + str(Ec))

print("CALCULADORA N°17")
#Calcular la Peso
#declarar
masa,gravedad = 0,0
#asignar
masa = 5
gravedad = 10
#calcular
peso = masa * gravedad
#mostrar
print("La masa es: " + str(masa))
print("La gravedad es: " + str(gravedad))
print("El peso es: " + str(peso))

print("CALCULADORA N°18")
#Halla la Fuerza de rozamiento
#declarar
u,N=0.0,0
#asignacion
u=0.5
N = 10
#calcular
Ffr=u*N
#mostrar
print("El coeficiente de roce es: " + str(u))
print("La normal es: " + str(N))
print("La fuerza de rozamiento es: " + str(Ffr))

print("CALCULADORA N°19")
#calcular la potencia
masaP,aceleracion,distancia,tiempo=0.0,0,0,0
#asignar
masaP=10
aceleracion=6
distancia=10
tiempo = 2
#calcular
fuerza=masaP*aceleracion
trabajo=fuerza*distancia
potencia = trabajo/tiempo
#mostrar
print("La masa es: " + str(masaP))
print("La aceleracion es: " + str(aceleracion))
print("La distancia es: " + str(distancia))
print("La fuerza es: " + str(fuerza))
print("El trabajo es: " + str(trabajo))
potencia ("La potencia es: " + str(potencia))

print("CALCULADORA N°20")
#calcular la superficie un cilindro
#declarar
pi,radioCil,alturaCi=0,0,0
#asignar
pi=3.14
radioCil=10
alturaCi=8
#calcular
Sci=2*pi*radioCil*alturaCi
#mostrar
print("El pi es: " + str(pi))
print("El radio es: " + str(radioCil))
print("La altura es: " + str(alturaCi))
print("La superficie de un cilindro es: " + str(Sci))










