#https://github/baptisteCanac
from turtle import *
from random import *
import turtle
import time
import random
from threading import Thread
import sys

wallet = 500
i = 0
while True:
	i += 1
	print("\n\n", i, "part")
	print('You have', wallet, "$ in your wallet")
	winner = ""
	pari = input('Who you think gonna win (blue, pink, yellow or green) : ')
	moneyBet = input('How much do you want to bet :')
	intMoneyBet = int(moneyBet)
	def betMoney():
		if intMoneyBet > wallet:
			print('You bet more than you have money in your wallet')
			sys.exit()
		else:
			pass

	betMoney()

	screen = Screen()
	title("Turtle Race")
	setup(800, 500)
	bgcolor("forestgreen")
	speed(0)

	penup()
	goto(-100, 205)
	color("white")
	write("TURTLE RACE", font=("Arial", 20, "bold"))

	goto(-350, 200)
	pendown()
	color("chocolate")
	begin_fill()
	for i in range(2):
		forward(700)
		right(90)
		forward(400)
		right(90)
	end_fill()

	gap_size = 20
	shape("square")
	penup()

	color("white")
	for i in range(10):
		goto(250,(170-(i*gap_size*2)))
		stamp()

	for i in range(10):
		goto(250+gap_size,((210-gap_size)-(i*gap_size*2)))
		stamp()

	color("black")
	for i in range(10):
		goto(250,(190-(i*gap_size*2)))
		stamp()

	for i in range(10):
		goto(251+gap_size,((190-gap_size)-(i*gap_size*2)))
		stamp()

	# blue turtle
	blueTurtle = Turtle()
	blueTurtle.color("cyan")
	blueTurtle.shape("turtle")
	blueTurtle.shapesize(1.5)
	blueTurtle.penup()
	blueTurtle.goto(-300, 150)
	blueTurtle.pendown()

	#pink turtle
	pinkTurtle = Turtle()
	pinkTurtle.color("magenta")
	pinkTurtle.shape("turtle")
	pinkTurtle.shapesize(1.5)
	pinkTurtle.penup()
	pinkTurtle.goto(-300, 50)
	pinkTurtle.pendown()

	#yellow turtle
	yellowTurtle = Turtle()
	yellowTurtle.color("yellow")
	yellowTurtle.shape("turtle")
	yellowTurtle.shapesize(1.5)
	yellowTurtle.penup()
	yellowTurtle.goto(-300, -50)
	yellowTurtle.pendown()

	#green turtle
	greenTurtle = Turtle()
	greenTurtle.color("lime")
	greenTurtle.shape("turtle")
	greenTurtle.shapesize(1.5)
	greenTurtle.penup()
	greenTurtle.goto(-300, -150)
	greenTurtle.pendown()

	time.sleep(1)

	# from fastest to slowest
	speeds = [10, 6, 3, 1]
	blueTurtleSpeed = random.choice(speeds)
	pinkTurtleSpeed = random.choice(speeds)
	yellowTurtleSpeed = random.choice(speeds)
	greenTurtleSpeed = random.choice(speeds)

	#race begin

	def blueTurtleRace():
		blueTurtle.speed(blueTurtleSpeed)
		blueTurtle.goto(220, 150)

	def pinkTurtleRace():
		pinkTurtle.speed(pinkTurtleSpeed)
		pinkTurtle.goto(220, 50)

	def yellowTurtleRace():
		yellowTurtle.speed(yellowTurtleSpeed)
		yellowTurtle.goto(220, -50)

	def greenTurtleRace():
		greenTurtle.speed(greenTurtleSpeed)
		greenTurtle.goto(220, -150)

	def checkWinner():
		while True:
			if blueTurtle.pos() == (220, 150):
				print('blue turtle as win')
				winner = "blue"
				if pari == winner:
					betWin()
				else:
					print('It was the wrong choice')
					betLost()
				break
			elif pinkTurtle.pos() == (220, 50):
				print('pink turtle as win')
				winner = "pink"
				if pari == winner:
					betWin()
				else:
					print('It was the wrong choice')
					betLost()
				break
			elif yellowTurtle.pos() == (220, -50):
				print('yellow turtle as win')
				winner = "yellow"
				if pari == winner:
					betWin()
				else:
					print('It was the wrong choice')
					betLost()
				break
			elif greenTurtle.pos() == (220, -150):
				print('green turtle as win')
				winner = "green"
				if pari == winner:
					betWin()
				else:
					print('It was the wrong choice')
					betLost()
				break
			else:
				continue

	def betWin():
		global intMoneyBet
		global wallet
		intMoneyBet = intMoneyBet * 2
		wallet += intMoneyBet
		print("You have now ", wallet, " $, in your wallet")

	def betLost():
		global intMoneyBet
		global wallet
		wallet -= intMoneyBet
		print("You have now ", wallet, " $ in your wallet")

	blueRace = Thread(target=blueTurtleRace)
	pinkRace = Thread(target=pinkTurtleRace)
	yellowRace = Thread(target=yellowTurtleRace)
	greenTurtleRace = Thread(target=greenTurtleRace)
	checkWinnerDef = Thread(target=checkWinner)

	blueRace.start()
	pinkRace.start()
	yellowRace.start()
	greenTurtleRace.start()
	checkWinnerDef.start()

	screen.mainloop()
