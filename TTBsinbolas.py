import turtle
import time
import random
import winsound
slow = 0.01

#marcador 
Score =0
High_Score=0
# Resetear marcador
def resetear():
	Score = 0
	texto.clear()
	texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))

## variables
anzuelos = [v_mina, v_mina1, v_mina2, v_mina3, v_mina4] 
Minas = [b_mina, b_mina1,  b_mina3,]
botellas = [b_mina2, b_mina4]
x = random.randint(-300,300)
y = random.randint(-300,300)
#pantalla
pantalla=turtle.Screen()
pantalla.bgpic("imagenes/fondo.gif")
pantalla.title("Tortuga TragaBolas")
pantalla.setup(width = 600, height = 600)

#Bucle for para registrar las imagenes
listagif = ["imagenes/blackhole.gif","imagenes/comida1.gif","imagenes/bomba.gif","imagenes/minamorada.gif",
"imagenes/comida.gif","imagenes/comida3.gif","imagenes/arrecife.gif","imagenes/botellas.gif"]
for i in listagif:
	pantalla.register_shape(i)


#cabeza de la tortuga
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
comida.shape("imagenes/comida1.gif")
comida.color("yellow")
comida.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida.goto(48,150) #cordenada donde comienza la cabeza
comida.direction = "stop"
comida.showturtle()

#Debuffs
#funcion para debiuffs
def debuff(mina):
	mina.speed(0)
	mina.shape("imagenes/minamorada.gif")
	mina.penup()  
	mina.goto(1000,1000) 
	mina.direction = "stop"
	mina.showturtle()
	


#Bombas
#funcion bomvas
def bomb(bomba):
	bomba.shape("imagenes/bomba.gif")
	bomba.color("black")
	bomba.penup()  
	bomba.goto(1000,1000) 
	bomba.direction = "stop"
	bomba.showturtle()
	bomba = turtle.Turtle()
def botl(botella):
	botella.speed(0)
	botella.shape("imagenes/botellas.gif")
	botella.color("black")
	botella.penup()  
	botella.goto(1000,1000) 
	botella.direction = "stop"
	botella.showturtle()


	
### para cada elemento un bucle para crearlos como elementos turtle
for a in anzuelos:
	a = turtle.Turtle()
	debuff(a)
for b in Minas:
	b= turtle.Turtle()
	bomb(b)
for t in botellas:
	t=turtle.Turtle()
	botl(t)
	

#Buffs
buff =turtle.Turtle()
buff.speed(0)
buff.penup()
buff.goto(700,700)
buff.shape("arrecife.gif")

buff.hideturtle()
 #Buff2



#Agujero de gusano
entrada =turtle.Turtle()
entrada.speed(0)
entrada.penup()
entrada.goto(700,700)
entrada.shape("imagenes/blackhole.gif")
entrada.hideturtle()

salida =turtle.Turtle()
salida.speed(0)
salida.penup()
salida.goto(700,700)
salida.shape("imagenes/blackhole.gif")
salida.color("black")
salida.hideturtle()
		#comida2
comida2 =turtle.Turtle()
comida2.speed(0)
comida2.shape("imagenes/comida.gif")
comida2.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida2.goto(700,700) #cordenada donde comienza la cabeza
comida2.direction = "stop"
comida2.showturtle()		

comida3 =turtle.Turtle()
comida3.speed(0)
comida3.shape("imagenes/comida3.gif")
comida3.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida3.goto(700,700) #cordenada donde comienza la cabeza
comida3.direction = "stop"
comida3.showturtle()	

#Texto de los marcadores
texto =turtle.Turtle()
texto.speed(0)
texto.color("blue")
texto.penup()
texto.hideturtle()
texto.goto(0,250)
texto.write("Score:0             High_Score: 0", align="center", font=("Comic_sans",18	,"normal"))


#Dibujar los limites del mapa
recinto = turtle.Turtle()
recinto.color("black")
recinto.speed(0)
recinto.hideturtle()
recinto.penup()
recinto.forward(300)
recinto.pendown()
recinto.left(90)
recinto.forward(300)
recinto.left(90)
recinto.forward(600)
recinto.left(90)
recinto.forward(600)
recinto.left(90)
recinto.forward(600)
recinto.left(90)
recinto.forward(300)


#Funciones, de movimiento y de interaccion con elementos
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

def Suicide():
	corazon.direction="stop"

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
def morir():
		winsound.PlaySound("sonidos/death", winsound.SND_FILENAME)
		corazon.color("black")
		corazon.goto(0,0)	
		corazon.write("Estás muerto",align="center", font=("Comic_sans",18	,"normal"))
		corazon.direction = "stop"	
		comida2.goto(700,700)
		buff.goto(700,700)
		entrada.goto(700,700)
		salida.goto(700,700)
		b_mina1.goto(700,700)
		v_mina1.goto(700,700)
		b_mina.goto(700,700)
		v_mina.goto(700,700)
		b_mina2.goto(700,700)
		v_mina2.goto(700,700)
		b_mina3.goto(700,700)
		v_mina3.goto(700,700)
		b_mina4.goto(700,700)
		v_mina4.goto(700,700)
		#Reinicio de la pantalla
		time.sleep(2)				
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")
				
				# Resetear marcador
		Score = 0
		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
		
#funcion comer
def comer():
	winsound.PlaySound("sonidos/comer", winsound.SND_FILENAME)
	
	comida2.goto(x,y)
	
	comida.goto(x,y)
	
#funcion comer2
def comer2():
	winsound.PlaySound("sonidos/comer", winsound.SND_FILENAME)
	
	comida3.goto(x,y)
	
	
#esta serie de comandos permite dectectar el teclado, y le asignamos dirrecciones.
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(derecha, "Left")
pantalla.onkeypress(izquierda, "Right")
pantalla.onkeypress(Teleport, "r")
pantalla.onkeypress(Suicide, "s")

#empieza el juego
while True:
	time.sleep(slow)		

	pantalla.update()
	
		#colisiones con los bordes
	if corazon.xcor()>300 or corazon.xcor()<-300 or corazon.ycor()>300 or corazon.ycor()<-300:
		morir()
		
		resetear()

		
		#Reinicio de la pantalla
		time.sleep(2)
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")

		
	#colision con la comida	
	if corazon.distance(comida) < 20:
		comer()
		Score +=1 
		if Score > High_Score:
			High_Score =Score
			texto.clear()
			texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	#colision con comida dos
	if corazon.distance(comida2) < 20:
		comer()
		Score +=1 
		if Score > High_Score:
			High_Score =Score
			texto.clear()
			texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	
	#colision comida 3
	if corazon.distance(comida3) < 20:
		comer2()
		Score +=10
		if Score > High_Score:
			High_Score =Score
			texto.clear()
			texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))


	mov()

	
	# Aparición de los buffs
	if Score >2:
		buff.goto(0,0)
		buff.showturtle()

		if corazon.distance(buff) < 20:
			winsound.PlaySound("sonidos/buff", winsound.SND_FILENAME)
			
			
			comida2.goto(x,y)
			x = random.randint(-500,500)
			y = random.randint(-500,500)
			comida3.goto(x,y)
	

	#agujero negro
	if Score >0:
		time.sleep(0.001)
		entrada.goto(-250,250)
		entrada.showturtle()
		salida.goto(250,-250)
		salida.showturtle()

		if corazon.distance(entrada)< 20 :
			winsound.PlaySound("sonidos/blackhole", winsound.SND_FILENAME)
			corazon.goto(200,-200)
			
		if corazon.distance(salida) < 20 :
			winsound.PlaySound("sonidos/blackhole", winsound.SND_FILENAME)
			corazon.goto(-200,200)
				

	# Aparición de Debuffs en funcion de la puntuacion

	if Score>0 <20:
		 
		
		
		v_mina.goto(x,y)
		
	if corazon.distance(v_mina) <20:
		v_mina.goto(700,700)
		
		
		b_mina.goto(x,y)
		
		
		b_mina1.goto(x,y)
		
		
		b_mina2.goto(x,y)
		
		
		b_mina3.goto(x,y)
		
		
		b_mina4.goto(x,y)
	
	if Score>= 10 <20:
		corazon.speed(0)
		
		v_mina1.goto(x,y)				

	if corazon.distance(v_mina1) <20:
		b_mina.goto(x,y)
				
		b_mina1.goto(x,y)
				
		b_mina2.goto(x,y)
			
		b_mina3.goto(x,y)
			
		b_mina4.goto(x,y)

	if Score>20:
		v_mina1.goto(-30,0)				

		v_mina.goto(30,0)
	for m in Minas:
		if corazon.distance(m)<40:
			morir()
	for m in botellas:
		if corazon.distance(m)<40:
			morir()
		 
