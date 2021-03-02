import turtle
import time
import random
import winsound
slow = 0.01

#marcador 
Score =0
High_Score=0

#pantalla
pantalla=turtle.Screen()
pantalla.bgpic("fondo.gif")
pantalla.title("Tortuga TragaBolas")
pantalla.setup(width = 600, height = 600)
pantalla.register_shape("blackhole.gif")
pantalla.register_shape("comida1.gif")
pantalla.register_shape("bomba.gif")
pantalla.register_shape("minamorada.gif")
pantalla.register_shape("comida.gif")
pantalla.register_shape("comida3.gif")
pantalla.register_shape("arrecife.gif")
pantalla.register_shape("botellas.gif")

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
comida.shape("comida1.gif")
comida.color("yellow")
comida.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida.goto(48,150) #cordenada donde comienza la cabeza
comida.direction = "stop"
comida.showturtle()

#Debuffs




v_mina = turtle.Turtle()
v_mina.speed(0)
v_mina.shape("minamorada.gif")
v_mina.penup()  
v_mina.goto(1000,1000) 
v_mina.direction = "stop"
v_mina.showturtle()

v_mina1 = turtle.Turtle()
v_mina1.speed(0)
v_mina1.shape("minamorada.gif")
v_mina1.penup()  
v_mina1.goto(1000,1000) 
v_mina1.direction = "stop"
v_mina1.showturtle()

v_mina2 = turtle.Turtle()
v_mina2.speed(0)
v_mina2.shape("minamorada.gif")
v_mina2.penup()  
v_mina2.goto(1000,1000) 
v_mina2.direction = "stop"
v_mina2.showturtle()

v_mina3 = turtle.Turtle()
v_mina3.speed(0)
v_mina3.shape("minamorada.gif")
v_mina3.penup()  
v_mina3.goto(1000,1000) 
v_mina3.direction = "stop"
v_mina3.showturtle()

v_mina4 = turtle.Turtle()
v_mina4.speed(0)
v_mina4.shape("minamorada.gif")
v_mina4.penup()  
v_mina4.goto(1000,1000) 
v_mina4.direction = "stop"
v_mina4.showturtle()

#Bombas
b_mina = turtle.Turtle()
b_mina.speed(0)
b_mina.shape("bomba.gif")
b_mina.color("black")
b_mina.penup()  
b_mina.goto(1000,1000) 
b_mina.direction = "stop"
b_mina.showturtle()

b_mina1 = turtle.Turtle()
b_mina1.speed(0)
b_mina1.shape("bomba.gif")
b_mina1.color("black")
b_mina1.penup()  
b_mina1.goto(1000,1000) 
b_mina1.direction = "stop"
b_mina1.showturtle()

b_mina2 = turtle.Turtle()
b_mina2.speed(0)
b_mina2.shape("botellas.gif")
b_mina2.color("black")
b_mina2.penup()  
b_mina2.goto(1000,1000) 
b_mina2.direction = "stop"
b_mina2.showturtle()

b_mina3 = turtle.Turtle()
b_mina3.speed(0)
b_mina3.shape("bomba.gif")
b_mina3.color("black")
b_mina3.penup()  
b_mina3.goto(1000,1000) 
b_mina3.direction = "stop"
b_mina3.showturtle()

b_mina4 = turtle.Turtle()
b_mina4.speed(0)
b_mina4.shape("botellas.gif")
b_mina4.color("black")
b_mina4.penup()  
b_mina4.goto(1000,1000) 
b_mina4.direction = "stop"
b_mina4.showturtle()

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
entrada.shape("blackhole.gif")
entrada.hideturtle()

salida =turtle.Turtle()
salida.speed(0)
salida.penup()
salida.goto(700,700)
salida.shape("blackhole.gif")
salida.color("black")
salida.hideturtle()
		#comida2
comida2 =turtle.Turtle()
comida2.speed(0)
comida2.shape("comida.gif")
comida2.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida2.goto(700,700) #cordenada donde comienza la cabeza
comida2.direction = "stop"
comida2.showturtle()		

comida3 =turtle.Turtle()
comida3.speed(0)
comida3.shape("comida3.gif")
comida3.penup() #penup se utiliza para borrar el rastro en el metodo turtle
comida3.goto(700,700) #cordenada donde comienza la cabeza
comida3.direction = "stop"
comida3.showturtle()	


#cuerpo serpiente a partir de una lista
segmentos = []



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

#esta serie de comandos permite dectectar el teclado, y le asignamos dirrecciones.
pantalla.listen()
pantalla.onkeypress(arriba, "Up")
pantalla.onkeypress(abajo, "Down")
pantalla.onkeypress(derecha, "Left")
pantalla.onkeypress(izquierda, "Right")
pantalla.onkeypress(Teleport, "r")
pantalla.onkeypress(Suicide, "s")


while True:
	time.sleep(slow)		

	pantalla.update()
	
		#colisiones con los bordes
	if corazon.xcor()>300 or corazon.xcor()<-300 or corazon.ycor()>300 or corazon.ycor()<-300:
		winsound.PlaySound("death", winsound.SND_FILENAME)
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
		for segmento in segmentos:
			segmento.goto(700,700)
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
		winsound.PlaySound("comer", winsound.SND_FILENAME)
		x = random.randint(-230,230)
		y = random.randint(-230,230)
		comida.goto(x,y)
		
		#se añade un nuevo segmento dentro del if y creamos con el una lista
		
		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("circle")
		nuevo_segmento.color("green")
		nuevo_segmento.penup() #penup se utiliza para borrar el rastro en el metodo turtle
		segmentos.append(nuevo_segmento)

		Score +=1 
		if Score > High_Score:
			High_Score =Score

		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	
	#colision con comida dos
	if corazon.distance(comida2) < 20:
		winsound.PlaySound("comer", winsound.SND_FILENAME)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
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
	
	if corazon.distance(comida3) < 20:
		winsound.PlaySound("comer", winsound.SND_FILENAME)
		x = random.randint(-800,800)
		y = random.randint(-800,800)
		comida3.goto(x,y)

	

		Score +=10
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
			winsound.PlaySound("death", winsound.SND_FILENAME)
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
	if len(segmentos) >2:
		buff.goto(0,0)
		buff.showturtle()

		if corazon.distance(buff) < 20:
			winsound.PlaySound("buff", winsound.SND_FILENAME)
			x = random.randint(-300,300)
			y = random.randint(-300,300)
			comida2.goto(x,y)
			x = random.randint(-500,500)
			y = random.randint(-500,500)
			comida3.goto(x,y)
	
			


	#agujero negro
	if len(segmentos)>0:
		time.sleep(0.001)
		entrada.goto(-250,250)
		entrada.showturtle()
		salida.goto(250,-250)
		salida.showturtle()

		if corazon.distance(entrada)< 20 :
			winsound.PlaySound("blackhole", winsound.SND_FILENAME)
			corazon.goto(200,-200)
			
		if corazon.distance(salida) < 20 :
			winsound.PlaySound("blackhole", winsound.SND_FILENAME)
			corazon.goto(-200,200)
				

	# Aparición de Debuffs

	if len(segmentos)>0:
		corazon.speed(0)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		v_mina.goto(x,y)
		
	if corazon.distance(v_mina) <20:
		v_mina.goto(700,700)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina1.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina2.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina3.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina4.goto(x,y)
	
	if len(segmentos)>= 10 <20:
		corazon.speed(0)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		v_mina1.goto(x,y)				

	if corazon.distance(v_mina1) <20:
		v_mina1.goto(700,700)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina1.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina2.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina3.goto(x,y)
		x = random.randint(-300,300)
		y = random.randint(-300,300)
		b_mina4.goto(x,y)

	if len(segmentos)>20:
		corazon.speed(0)
		v_mina1.goto(0,0)				

	

			 
	if corazon.distance(b_mina)<40: #muerte por mina negra
		winsound.PlaySound("death", winsound.SND_FILENAME)
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
		for segmento in segmentos:
			segmento.goto(1000,1000)
			
		segmentos.clear()
				#Reinicio de la pantalla
		
				#Reinicio de la pantalla
		time.sleep(2)				
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")
				
				# Resetear marcador
		Score = 0
		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
			
	if corazon.distance(b_mina1) <40: 
		winsound.PlaySound("death", winsound.SND_FILENAME)
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
		
		for segmento in segmentos:
			segmento.goto(1000,1000)
			
		segmentos.clear()
				#Reinicio de la pantalla
				#Reinicio de la pantalla
		time.sleep(2)				
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")
				
				# Resetear marcador
		Score = 0
		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	
	if corazon.distance(b_mina2)<40 : 
		winsound.PlaySound("death", winsound.SND_FILENAME)
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
		
		for segmento in segmentos:
			segmento.goto(1000,1000)
		
		segmentos.clear()
				#Reinicio de la pantalla
				#Reinicio de la pantalla
		time.sleep(2)				
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")
				
				# Resetear marcador
		Score = 0
		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))
	
	if corazon.distance(b_mina3)<40 :
		winsound.PlaySound("death", winsound.SND_FILENAME)
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
	
	if corazon.distance(b_mina4)<40 :
		winsound.PlaySound("death", winsound.SND_FILENAME)
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
		
		for segmento in segmentos:
			segmento.goto(1000,1000)
			
		segmentos.clear()
				#Reinicio de la pantalla
				#Reinicio de la pantalla
		time.sleep(2)				
		corazon.clear()
		corazon.shape("turtle")
		corazon.color("green")
				
				# Resetear marcador
		Score = 0
		texto.clear()
		texto.write("Score: {}            High_Score: {}".format(Score, High_Score), align="center", font=("Comic_sans",18	,"normal"))