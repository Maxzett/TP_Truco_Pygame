import pygame, sys, csv
from modules.constantes import *
from modules.auxiliares import *
#from modules.ranking import registrar_resultado


def mostrar_ranking():
    """Muestra la pantalla de ranking con datos leídos de un archivo CSV."""
    pygame.display.set_caption("Ranking Jugadores")
    
    corriendo = True
    ruta_csv = "ranking.csv"  # Archivo CSV con los datos del ranking
    boton_volver = pygame.Rect(ANCHO // 2 - 150, ALTO - 100, 300, 50)

    while corriendo:
        pantalla.fill(BACKGROUND_RANKING)
        mouse_pos = pygame.mouse.get_pos()

        # Título del ranking
        dibujar_texto("Ranking de Jugadores", FUENTE_TITULO, NEGRO, pantalla, ANCHO // 2, 50)

        # Leer datos del archivo CSV
        try:
            with open(ruta_csv, "r") as archivo_csv:
                lector_csv = csv.reader(archivo_csv)
                datos = list(lector_csv)
        except FileNotFoundError:
            datos = [["Sin datos disponibles"]]

        # Mostrar los datos en pantalla
        y_offset = 150
        for fila in datos:
            texto = " | ".join(fila)
            dibujar_texto(texto, FUENTE_RANKING, NEGRO, pantalla, ANCHO // 2, y_offset)
            y_offset += 40

        # Dibujar el botón para volver al menú
        color_boton = VERDE_CLARO if boton_volver.collidepoint(mouse_pos) else LILA
        pygame.draw.rect(pantalla, color_boton, boton_volver)
        dibujar_texto('Volver', FUENTE_BOTON, NEGRO, pantalla, boton_volver.centerx, boton_volver.centery)
        
        # Manejo de eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Click izquierdo
                    if boton_volver.collidepoint(evento.pos):
                        corriendo = False

        # Actualizar pantalla
        pygame.display.flip()
        
def iniciar_juego():
    pygame.display.set_caption("Juego de Truco")
    
    #registro de nombre jugador
    nombre_jugador = entrada_nombre()
    
    #seleccion de puntos
    puntos_objetivo = elegir_puntos()

    pantalla.fill(AZUL)
    #resumen nombre y puntos selccionados
    dibujar_texto(f"¡Hola, {nombre_jugador}!", FUENTE, NEGRO, pantalla, ANCHO // 2, ALTO // 2 - 50)
    dibujar_texto(f"Jugaremos a {puntos_objetivo} puntos.", FUENTE, NEGRO, pantalla, ANCHO // 2, ALTO // 2 + 50)
    pygame.display.flip()
    pygame.time.wait(2000)
    
    
    
    # Configuración del juego
    reloj = pygame.time.Clock()
    mazo = crear_mazo()  # Crear el mazo
    # Mezclar las cartas
    mezclar(mazo) 
    # Repartir las cartas
    cartas_jugador, cartas_maquina = repartir(mazo)
    
    
    # Puntos iniciales
    puntos_totales_jugador = 0
    puntos_totales_maquina = 0
    mensaje_envido = ""
    tiempo_mostrar_mensaje = 0
    
    envido_dispoible = True
    
    # Pantalla principal del juego
    while puntos_totales_jugador < puntos_objetivo and puntos_totales_maquina < puntos_objetivo:
        pantalla.fill(VERDE)  #Fondo verde para simular una mesa
        mouse_pos = pygame.mouse.get_pos()
        
        #asignar mano
        #primer_mano = random.choice(["jugador", "maquina"])
        
        
        
       
        
        # Mostrar información del juego
        dibujar_texto(f"Jugador: {nombre_jugador}", FUENTE_JUEGO, BLANCO, pantalla, 175, 30)
        dibujar_texto(f"Puntos objetivo: {puntos_objetivo}", FUENTE_JUEGO, BLANCO, pantalla, 175, 70)

        # Mostrar puntos en la esquina superior derecha
        dibujar_texto(f"{puntos_totales_jugador} - {puntos_totales_maquina}", FUENTE_JUEGO, BLANCO, pantalla, ANCHO - 100, 30)
        
        # Mostrar las cartas de la máquina (boca abajo)
        mostrar_cartas(cartas_maquina, ANCHO // 2 - 175, 50, boca_arriba=False)
        
        # Mostrar las cartas del jugador (boca arriba)
        mostrar_cartas(cartas_jugador, ANCHO // 2 - 175, ALTO - 200, boca_arriba=True)
        
        # Dibujar y actualizar color de los botones del juego
        actualizar_color_botones(botones_juego, mouse_pos, pantalla, FUENTE_BOTON, LILA, VERDE_CLARO)
        
        # Mostrar mensaje si existe y está en tiempo
        if mensaje_envido and pygame.time.get_ticks() - tiempo_mostrar_mensaje < 5000:  # Mostrar por 5 segundos
            dibujar_texto(mensaje_envido, FUENTE_JUEGO, BLANCO, pantalla, ANCHO // 2, ALTO // 2)
        elif mensaje_envido:  # Limpiar mensaje tras 5 segundos
            mensaje_envido = ""
        
        # Detectar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Clic izquierdo
                    for boton in botones_juego:
                        if boton["rect"].collidepoint(evento.pos):
                            if boton["texto"] == "Envido":
                                if envido_dispoible == True:
                                    tantos_jugador = calcular_puntaje_envido(cartas_jugador)
                                    tantos_maquina = calcular_puntaje_envido(cartas_maquina)
                                    if tantos_jugador > tantos_maquina:
                                        puntos_totales_jugador += 2
                                        mensaje_envido = f"{nombre_jugador} ganó el Envido con {tantos_jugador} puntos"
                                    elif tantos_maquina > tantos_jugador:
                                        puntos_totales_maquina += 2
                                        mensaje_envido = f"La máquina ganó el Envido con {tantos_maquina} puntos"
                                    else:
                                        dibujar_texto(f"X gana porque es mano", FUENTE_JUEGO, BLANCO, pantalla, 300, ALTO - 200)
                                    
                                    envido_dispoible = False
                                tiempo_mostrar_mensaje = pygame.time.get_ticks()
                                  
                            elif boton["texto"] == "Truco":
                                print("Se presionó 'Truco'")

        # Actualizar pantalla
        pygame.display.flip()
        reloj.tick(30)