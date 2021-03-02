import turtle
import time
import random

slow = 0.2

#marcador 
Score =0
High_Score=0

#pantalla
pantalla=turtle.Screen()
pantalla.bgcolor("violet")
pantalla.title("Tortuga TragaBolas")
pantalla.setup(width = 500, height = 500)

#serpiente
corazon =turtle.Turtle()
corazon.speed(0)
corazon.shape("turtle")
corazon.color("green")
corazon.penup() #penup se utiliza para borrar el rastro en el metodo turtle
corazon.goto(0,0) #cordenada donde comienza la cabeza
corazon.direction = "stop"
corazon.showturtle()

#comida
comida =turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("yellow")
comida.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida.goto(48,150) #cordenada donde comienza la cabeza
comida.direction = "stop"
comida.showturtle()

#Buffs
buff =turtle.Turtle()
buff.speed(0)
buff.penup()
buff.goto(700,700)
buff.shape("square")
buff.color("brown")
buff.hideturtle()

		#comida2
comida2 =turtle.Turtle()
comida2.speed(0)
comida2.shape("circle")
comida2.color("white")
comida2.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida2.goto(700,700) #cordenada donde comienza la cabeza
comida2.direction = "stop"
comida2.showturtle()		
#cuerpo serpiente a partir de una lista
segmentos = []

#Texto de los marcadores
texto =turtle.Turtle()
texto.speed(0)
texto.color("blue")
texto.penup()
texto.hideturtle()
texto.goto(0,215)
texto.write("Score:0             High_Score: 0", align="center", font=("Comic_sans",18	,"normal"))


#Funciones, primero se crea una funcion de movimiento up
def arriba():
	corazon.direction ="up"
def abajo():
	corazon.direction ="down"
def derecha():
	corazon.direction ="right"
def izquierda(): 
	corazon.direction ="left"
def Teleport():
	corazon.direction ="teleport"



def mov():
	if corazon.direction == "up":
		y= corazon.ycor() #ESTE COMANDO INFORMA DE LA LOCALIZACION DE LA VARIABLE
		corazon.sety(y + 20)#EL DESPLAZAMIENTO ES POR PIXELES.
		corazon.seth(90)
	if corazon.direction == "down":
		y= corazon.ycor()  
		corazon.sety(y + -20)
		corazon.seth(270)
	if corazon.direction == "right":
		x= corazon.xcor()  
		corazon.setx(x - 20)
		corazon.seth(180)	
	if corazon.direction == "left":
		x= corazon.xcor()  
		corazon.setx(x + 20)
		corazon.seth(360)
	if corazon.direction == "teleport":
		x = random.randint(-230,230)
		y = random.randint(-230,230)
		corazon.goto(x,y)
		#corazon.direction = "stop"		

#esta serie de comandos permite dectectar el teclado, y le asignamos dirrecciones.
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(derecha, "Left")
pantalla.onkeypress(izquierda, "Right")
pantalla.onkeypress(Teleport, "r")
while True:
	pantalla.update()

	#colisiones con los bordes
	if corazon.xcor()>240 or corazon.xcor()<-240 or corazon.ycor()>240 or corazon.ycor()<-240:
		time.sleep(1)
		corazon.color("black")
		corazon.goto(0,0)	
		corazon.write("Estás muerto",align="center", font=("Comic_sans",18	,"normal"))
		corazon.direction = "stop"	

		for segmento in segmentos:
			segmento.goto(1000,1000)
		#lista segmentos
		segmentos.clear()
		
		#Reinicio de la pantalla
		time.sleep(2)
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")

	

		# Resetear marcador
		Score = 0
		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))


	#colision con la comida	
	if corazon.distance(comida) < 20:
		x = random.randint(-230,230)
		y = random.randint(-230,230)
		comida.goto(x,y)

		#se añade un nuevo segmento dentro del if y creamos con el una lista
		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("circle")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup() #penup se utiliza para borrar el rastro en el metodo turtle
		segmentos.append(nuevo_segmento)

		Score +=1 
		if Score > High_Score:
			High_Score =Score

		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	
	#colision con comida dos
	if corazon.distance(comida2) < 20:
	
		x = random.randint(-230,230)
		y = random.randint(-230,230)
		comida2.goto(x,y)

		#se añade un nuevo segmento dentro del if y creamos con el una lista
		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("circle")
		nuevo_segmento.color("grey")
		nuevo_segmento.penup() #penup se utiliza para borrar el rastro en el metodo turtle
		segmentos.append(nuevo_segmento)

		Score +=1 
		if Score > High_Score:
			High_Score =Score

		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	
	#mover el cuerpo
	totalSeg =len(segmentos)
	for index in range(totalSeg -1,0,-1):
		x= segmentos[index -1].xcor()
		y= segmentos[index -1].ycor()	
		segmentos[index].goto(x,y)

	if totalSeg >0:
		x =corazon.xcor()
		y =corazon.ycor()
		segmentos[0].goto(x,y)

	mov()

	#Colisiones con el cuerpo
	for segmento in segmentos:
		if segmento.distance(corazon)<20:
			time.sleep(0.5)
			corazon.color("black")
			corazon.goto(0,0)	
			corazon.write("Estás muerto",align="center", font=("Comic_sans",18	,"normal"))
			corazon.direction = "stop"	




			for segmento in segmentos:
				segmento.goto(1000,1000)
			
			segmentos.clear()
				#Reinicio de la pantalla
			time.sleep(2)
			corazon.clear()
			corazon.shape("turtle")
			corazon.color("green")

		# Resetear marcador
			Score = 0
			texto.clear()
			texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))

	# Aparición de los buffs
	if len(segmentos) >3:
		buff.goto(0,0)
		buff.showturtle()

		if corazon.distance(buff) < 20:
			buff.goto(700,700)
			buff.hideturtle()
			comida2.goto(75,100)

	time.sleep(slow)

