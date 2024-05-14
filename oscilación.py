import pgzrun
import pygame
import math

TITLE = "Hola"
WIDTH = 800
HEIGHT = 600

# Define las propiedades del objeto
ball = Actor('hair_0')
ball.pos = WIDTH // 2, HEIGHT // 2
amplitude = 100  # Amplitud de la oscilación
frequency = 1  # Frecuencia de la oscilación
time = 0  # Tiempo inicial

def update(delta):
    global time
    
    # Incrementa el tiempo
    time += delta / 1000
    
    # Calcula la nueva posición vertical basada en la función seno
    ball.y = HEIGHT // 2 + amplitude * math.sin(2 * math.pi * frequency * time)

def draw():
    screen.clear()
    ball.draw()

pgzrun.go() 