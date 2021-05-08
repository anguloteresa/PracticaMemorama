# María Teresa Angulo Tello
# A00825411

# Reflexión
# En este programa pude poner en práctica todos los conocimientos hasta este momento del uso
# de la librería freegames. Me di cuenta de que realizar este juego es bastante sencillo si se
# utilizan ciclos para dibujar las cartas dentro de nuestro canvas, en lugar de ir dibujando cada una de las
# cartas en nuestro tablero de forma manual. Además, aprendí sobre el manejo de eventos al momento de hacer clic
# en nuestro mouse, y cómo se pueden calcular con exactitud las coordenadas en las que hemos hecho clic en el tablero.
# Sin dudas, esta semana tec fue bastante enriquecedora, y honestamente me he quedado con ganas de aprender más sobre algunos
# algoritmos, mucho más específicamente, sobre la inteligencia de los fantasmas dentro del juego de pacman. 
# freegames hace muy sencillo el desarrollo de estos juegos y creo que es una manera muy enriquecedora de adentrarse a este mundo,
# mientras se ponen en práctica algunos conceptos básicos de programación, escalando poco a poco en la dificultad de los mismos.

# Fecha   07/05/2020

from random import *
from turtle import *
from freegames import path

# Acceso al video
# https://drive.google.com/drive/folders/1LpquydrytUU5PhVUpUMnDJ0Ib7Gfymn6?usp=sharing
# Acceso al repositorio
# https://github.com/TwiliShiba/PracticaMemorama.git

# Kaeya Nation for the win
# Importar imágenes de la librería freegames
kaeya = path('kaeya.gif')
blank = path('blank.gif')
# Declarar el arreglo de las cartas, duplicadas
tiles = ['😄', '🤡', '👀', '👋🏼', '🐱', '🙉', '🐌', '🐙', 
        '🦋', '🐇', '🐲', '🍕', '🎱', '🚒', '🎡', '🕰', 
        '🔫', '💕', '🟦', '🐺', '🦔', '🐷', '🐶', '🐼', 
        '🐻', '🦊', '🐨', '🐝', '🐧', '🦉', '🐗', '🦁'
        ] * 2
# Inicializar la carta visible en ese momento como None
state = {'mark': None}
# Declarar un arreglo booleano de las cartas escondidas
hide = [True] * 64
# Contador para el número de veces que le hemos picado 
taps = 0
# Variable writer de clase Turtle para dibujar texto
writer = Turtle(visible = False)

# Dibuja un cuadrado con 50 de longitud de los lados en la coordenada colocada
def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'purple')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

# Convertir las coordenadas de donde dimos tap a un índice dentro de nuestro de nuestro arreglo
def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

# Convertir el conteo de cartas en coordenadas (x, y)
def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

# Función callback cuando das clic sobre la ventana
def tap(x, y):
    # Permit eusar las variables dentro y fuera de la función
    global mark, taps
    # Imprime la coordenada en la terminal
    print(x, y)
    # Aumenta el contador con cada clic
    taps = taps + 1
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    # Si mark es None o si mark == spot el usuario dió clic en la misma carta al índice sobre el
    # cuál el usuario dio clic o si la carta que ya está marcada es diferente a la seleccionada
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        # El estado ahora cambia a la carta donde el usuario dio clic
        state['mark'] = spot
    else:
        # Quiere decir que los dos son pares y las hace visibles
        hide[spot] = False
        hide[mark] = False
        # Vuelve mark a none, que no tenemos una carta visible
        state['mark'] = None

def nombre():
    writer.up()
    writer.goto(-110,-120)
    writer.color('blue')
    writer.write('Tere Angulo Tello - A00825411', align='left', font=('Arial', 16, 'normal'))

def win():
    clear()
    goto(0, 0)
    shape(blank)
    stamp()

def draw():
    global mark
    "Draw image and tiles."
    # Limpia toda la ventana
    clear()
    # Mueve turtle a la posicion 0, 0
    goto(0, 0)
    # Carga la imagen del auto en el turtle shape
    shape(kaeya)
    # Stamp a copy of the turtle shape onto the canvas at the current turtle position,
    # dibuja la imagen, el centro de la imagen(foto) se pone en la coordenada donde está la turtle
    stamp()

    # dibuja las 64 cartas de la memorama (tapando la imagen del auto)
    # inicialmente todas las cartas están escondidas - por lo tanto tapan el auto
    contador = 0
    for count in range(64):
        # si todavía no está descubierta la carta su valor será True
        if hide[count]:
            # calcula la esquina inferior izquierda donde se dibujará la carta
            x, y = xy(count)
            # dibuja un square en x, y - esquina inf. izq
            square(x, y)
            # dibuja el valor de la casilla
            # cuenta la cantidad de cartas escondidas
            contador = contador + 1

    # qué almacena state?
    # none    - no hay carta visible
    # ####### - index de la carta visible
    mark = state['mark']

    # Despliega la carta donde se dio el clic siempre y cuando no esté visible
    # si el estado no es None y esa carta no está descubierta
    if mark is not None and hide[mark]:
        # calcula la posición x, y de la carta
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        # depsliega en esa posicion x + 2, y el número de la carta oculta
        write(tiles[mark], font=('Arial', 30, 'normal'))

    escondidas = hide.count(True)
    print("Sin encontrar = ", escondidas)
    
    if escondidas == 0:
        win()
        up()
        goto(-75, 40)
        color('green')
        write('¡Ganaste!', font=('Arial', 30, 'normal'))
        goto(-95, -20)
        color('brown')
        write('¡Felicidades!', font=('Arial', 30, 'normal'))
        goto(-100, -80)
        color('red')
        write(f'Hiciste {taps} clics', font=('Arial', 30, 'normal'))
        nombre()
        return
    
    update()
    ontimer(draw, 100)

# Descomentar la siguiente línea para mezclar las cartas
# shuffle(tiles)
setup(420, 420, 370, 0)
addshape(kaeya)
addshape(blank)
hideturtle()        # Esconde la tortuga
tracer(False)       # Esconde el trazo
onscreenclick(tap)  # Registra los eventos hechos por el mouse
draw()
done()