import pygame, sys
from modules.constantes import *
from modules.funciones import *

pygame.init() #inicializar pygmae

pygame.display.set_caption("Truco | menu principal") #titulo de la ventana
pygame.font.init()

ejecutar = True
while ejecutar == True:
    #asigno el color a la ventana
    pantalla.fill(AZUL)
    # Obtener la posición del mouse 
    mouse_pos = pygame.mouse.get_pos()

    # Título del menú
    dibujar_texto("Menú Principal", FUENTE_TITULO, BLANCO, pantalla, ANCHO // 2, 100)
    dibujar_texto("Seleccione una opcion:", FUENTE, BLANCO, pantalla, ANCHO // 2, 200)

    actualizar_color_botones(botones_menu, mouse_pos, pantalla, FUENTE_BOTON, ROSA, VERDE_CLARO)
    
    # Manejo de eventos
    for evento in pygame.event.get():
        #salir con la X de la esquina
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1:  # Click izquierdo
                for boton in botones_menu:
                    if boton["rect"].collidepoint(evento.pos):
                        if boton["texto"] == "Iniciar nuevo juego":
                            print("Iniciando nuevo juego...")
                            iniciar_juego()
                            # Aquí puedes llamar a la función para iniciar el juego
                        elif boton["texto"] == "Ver ranking":
                            print("Mostrando ranking...")
                            mostrar_ranking()
                            # Aquí puedes llamar a la función para mostrar el ranking
                        elif boton["texto"] == "Salir":
                            pygame.quit()
                            sys.exit()


    pygame.display.update() #actualizo pantalla
pygame.quit() #apagar pygame