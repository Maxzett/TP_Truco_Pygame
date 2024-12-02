import pygame

# Dimensiones de la pantalla
ANCHO, ALTO = 1200, 800
pantalla = pygame.display.set_mode((ANCHO, ALTO))

#estructura de los botones
botones_menu = [
        {"texto": "Iniciar nuevo juego", "rect": pygame.Rect( ANCHO // 2 - 150, 300, 300, 50)},
        {"texto": "Ver ranking", "rect": pygame.Rect( ANCHO // 2 - 150, 400, 300, 50)},
        {"texto": "Salir", "rect": pygame.Rect( ANCHO // 2 - 150, 500, 300, 50)}
]  
botones_juego = [
    {"texto": "Envido", "rect": pygame.Rect(50, ALTO - 200 + 50, 200, 50)},
    {"texto": "Truco", "rect": pygame.Rect(ANCHO - 250, ALTO - 200 + 50, 200, 50)}
]
botones_puntos = [
        {"texto": "15 Puntos", "rect": pygame.Rect( ANCHO // 2 - 150, 300, 300, 50)},
        {"texto": "30 Puntos", "rect": pygame.Rect( ANCHO // 2 - 150, 400, 300, 50)},
]
botones_confirmar = [
    {"texto": "Confirmar", "rect": pygame.Rect(ANCHO // 2 - 100, 400, 200, 50)}
]

# Colores
BLANCO = (254, 250, 224)
NEGRO = (0, 0, 0)

AZUL = (53, 80, 112)
VIOLETA = (109, 89, 122)
LILA = (229, 107, 111)
SALMON = (229, 107, 111)
CREMA = (234, 172, 139)
VERDE = (0, 100, 0)
VERDE_CLARO = (96, 108, 56)

ROJO = (255, 0, 0)
ROSA = (239, 71, 111) 

GRIS = (180, 180, 180)
GRIS_CLARO = (220, 220, 220)
#Color fondo
FONDO = (0, 95, 115)
BACKGROUND_RANKING = (255, 209, 102)


# Fuente
pygame.font.init()
FUENTE_TITULO = pygame.font.Font(None, 80)
FUENTE = pygame.font.Font(None, 50)
FUENTE_JUEGO = pygame.font.Font(None, 45)
FUENTE_BOTON = pygame.font.Font(None, 40)
FUENTE_RANKING = pygame.font.Font(None, 30)

PALOS = ("Espada", "Basto", "Oro", "Copa")
VALORES = (1, 2, 3, 4, 5, 6, 7, 10, 11, 12)
JERARQUIA = {
    (1, "Espada"): 14, (1, "Basto"): 13, 
    (7, "Espada"): 12, (7, "Oro"): 11,   
    (3, "Espada"): 10, (3, "Basto"): 10, (3, "Oro"): 10, (3, "Copa"): 10,  
    (2, "Espada"): 9, (2, "Basto"): 9, (2, "Oro"): 9, (2, "Copa"): 9,      
    (1, "Oro"): 8, (1, "Copa"): 8,
    (12, "Espada"): 7, (12, "Basto"): 7, (12, "Oro"): 7, (12, "Copa"): 7,
    (11, "Espada"): 6, (11, "Basto"): 6, (11, "Oro"): 6, (11, "Copa"): 6,
    (10, "Espada"): 5, (10, "Basto"): 5, (10, "Oro"): 5, (10, "Copa"): 5,
    (7, "Basto"): 4, (7, "Copa"): 4,
    (6, "Espada"): 3, (6, "Basto"): 3, (6, "Oro"): 3, (6, "Copa"): 3,
    (5, "Espada"): 2, (5, "Basto"): 2, (5, "Oro"): 2, (5, "Copa"): 2,
    (4, "Espada"): 1, (4, "Basto"): 1, (4, "Oro"): 1, (4, "Copa"): 1,
}
# Prioridades de Truco (cartas "más fuertes")
PRIORIDAD_TRUCO = {
    "1Espadas": 14, "1Bastos": 13, "7Espadas": 12, "7Oros": 11,
    "3": 10, "2": 9, "1": 8, "12": 7, "11": 6, "10": 5,
    "7": 4, "6": 3, "5": 2, "4": 1
}
