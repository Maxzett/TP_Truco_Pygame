import random, pygame, sys
from modules.constantes import *

def dibujar_texto(texto: str, fuente, color, superficie, x, y) -> None:
    """Dibuja un texto en la superficie."""
    texto_obj = fuente.render(texto, True, color)
    texto_rect = texto_obj.get_rect(center=(x, y))
    superficie.blit(texto_obj, texto_rect)

def entrada_nombre() -> str:
    """Pantalla para registrar el nombre del jugador."""
    reloj = pygame.time.Clock()
    input_activo = True
    texto_entrada = ""
    max_caracteres = 15  # Limitar la longitud del nombre

    while input_activo:
        pantalla.fill(VIOLETA)
        mouse_pos = pygame.mouse.get_pos()        # Título
        dibujar_texto("Ingrese su nombre:", FUENTE, NEGRO, pantalla, ANCHO // 2, 200)

        # Mostrar cuadro de texto
        cuadro_rect = pygame.Rect(ANCHO // 2 - 200, 300, 400, 60)
        pygame.draw.rect(pantalla, GRIS, cuadro_rect)
        dibujar_texto(texto_entrada, FUENTE, NEGRO, pantalla, cuadro_rect.centerx, cuadro_rect.centery)

        # Botón "Confirmar"
        boton_confirmar = pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)
        pygame.draw.rect(pantalla, GRIS, boton_confirmar)
        dibujar_texto("Confirmar", FUENTE, NEGRO, pantalla, boton_confirmar.centerx, boton_confirmar.centery)

        actualizar_color_botones(botones_confirmar, mouse_pos, pantalla, FUENTE, ROSA, VERDE_CLARO)
        
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_BACKSPACE:  # Borrar último carácter
                    texto_entrada = texto_entrada[:-1]
                elif evento.key == pygame.K_RETURN:  # Confirmar con Enter
                    if texto_entrada.strip():  # No permitir confirmar si está vacío
                            input_activo = False
                else:
                    if len(texto_entrada) < max_caracteres:
                        texto_entrada += evento.unicode

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if boton_confirmar.collidepoint(evento.pos):  # Confirmar con el botón
                        if texto_entrada.strip():  # No permitir confirmar si está vacío
                            input_activo = False

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(30)

    return texto_entrada

def elegir_puntos() -> int:
    """Pantalla para seleccionar los puntos del juego."""
    reloj = pygame.time.Clock()
    seleccion = None
    while seleccion is None:
        pantalla.fill(VIOLETA)
        mouse_pos = pygame.mouse.get_pos()
        # Título
        dibujar_texto("¿A cuántos puntos quieres jugar?", FUENTE, NEGRO, pantalla, ANCHO // 2, 200)

        # Botón 15 puntos
        boton_15 = pygame.Rect(ANCHO // 2 - 100, 300, 200, 50)                
        pygame.draw.rect(pantalla, GRIS, boton_15)
        dibujar_texto("15 Puntos", FUENTE, NEGRO, pantalla, boton_15.centerx, boton_15.centery)

        # Botón 30 puntos
        boton_30 = pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)
        pygame.draw.rect(pantalla, GRIS, boton_30)
        dibujar_texto("30 Puntos", FUENTE, NEGRO, pantalla, boton_30.centerx, boton_30.centery)

        actualizar_color_botones(botones_puntos, mouse_pos, pantalla, FUENTE, ROSA, VERDE_CLARO)
        
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if boton_15.collidepoint(evento.pos):
                        seleccion = 15
                    elif boton_30.collidepoint(evento.pos):
                        seleccion = 30

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(30)

    return seleccion

def alternar_mano(mano_actual: str, jugador: str, maquina: str) -> str:
    if mano_actual == jugador:
        return maquina
    else:
        return jugador

def crear_mazo() -> list:
    mazo = [(valor, palo) for valor in VALORES for palo in PALOS ]
    return mazo

def mezclar(mazo: list) -> list:
    #Devuelve la secuencia pasada como argumento desordenada.
    #Cambia la lista y no devuelve una nueva
    random.shuffle(mazo)
    return mazo

def repartir(mazo: list) -> list:
    #usa slicing para tomar elementos
    jugador = mazo[0:3] #index 0,1,2
    maquina = mazo[3:6]#index 3,4,5
    return jugador, maquina

# Calcular puntos de envido
def calcular_puntaje_envido(cartas: list) -> int:
    #dict de equivalencias para envido
    valores = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 10: 0, 11: 0, 12: 0}
    palos = {}
    
    for valor, palo in cartas:
        if palo not in palos:
            palos[palo] = []
        palos[palo].append(valores[valor])

    max_puntaje = 0
    for palo, cartas_palo in palos.items():
        if len(cartas_palo) > 1:
            cartas_palo.sort(reverse=True)
            max_puntaje = max(max_puntaje, 20 + cartas_palo[0] + cartas_palo[1])
        else:
            max_puntaje = max(max_puntaje, cartas_palo[0])

    return max_puntaje

# Función para cargar y escalar imágenes
def cargar_imagen(ruta: str, ancho: int, alto: int) -> any:
    imagen = pygame.image.load(ruta)
    return pygame.transform.scale(imagen, (ancho, alto))

# Función para mostrar cartas en pantalla
def mostrar_cartas(cartas: list, x: int, y: int, boca_arriba: bool) -> None:
    ancho_carta = 100
    alto_carta = 150
    for i, carta in enumerate(cartas):
        if boca_arriba:
            ruta_carta = f"assets/images/{carta[0]} de {carta[1]}.jpg"
        else:
            ruta_carta = "assets/images/dorso_carta.jpg"
        imagen_carta = cargar_imagen(ruta_carta, ancho_carta, alto_carta)
        carta_x = x + i * (ancho_carta + 20)
        carta_y = y
        # Detectar si el mouse está sobre la carta
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if carta_x <= mouse_x <= carta_x + ancho_carta and carta_y <= mouse_y <= carta_y + alto_carta:
            if boca_arriba == True:
                imagen_carta = pygame.transform.scale(imagen_carta, (ancho_carta, alto_carta + 10))  # Elevar carta
        pantalla.blit(imagen_carta, (carta_x, carta_y))

#Funcion para cambiar color de botones al pararse sobre ellos 
def actualizar_color_botones(botones, mouse_pos: tuple, pantalla: any, fuente: any, color_normal: tuple, color_hover: tuple) -> None:
    """
    Actualiza el color de los botones dependiendo de si el mouse está sobre ellos.

    :param botones: Lista de diccionarios que representan los botones. Cada botón debe tener:
                    - "rect": pygame.Rect que define la posición y tamaño del botón.
                    - "texto": Texto que se mostrará en el botón.
    :param mouse_pos: Tupla con la posición actual del mouse (x, y).
    :param pantalla: Objeto de la pantalla de pygame donde se dibujarán los botones.
    :param fuente: Fuente de texto para los textos de los botones.
    :param color_normal: Color del botón en estado normal (cuando el mouse no está sobre él).
    :param color_hover: Color del botón cuando el mouse está sobre él.
    """
    for boton in botones:
        # Cambiar color si el mouse está sobre el botón
        color_boton = color_hover if boton["rect"].collidepoint(mouse_pos) else color_normal
        pygame.draw.rect(pantalla, color_boton, boton["rect"])
        dibujar_texto(boton["texto"], fuente, NEGRO, pantalla, boton["rect"].centerx, boton["rect"].centery)

# Función para determinar la jerarquía de las cartas
def comparar_cartas(carta1, carta2):
    jerarquia = {1: 14, 2: 9, 3: 10, 4: 1, 5: 2, 6: 3, 7: 11, 10: 4, 11: 5, 12: 6}
    return jerarquia[carta1[0]] - jerarquia[carta2[0]]

