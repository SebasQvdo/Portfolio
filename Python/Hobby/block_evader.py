import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ANCHO, ALTO = 600, 400
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Esquiva los enemigos!")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (200, 50, 50)
AZUL = (50, 50, 200)

# Jugador
jugador = pygame.Rect(50, ALTO//2, 40, 40)
vel_jugador = 5

# Enemigos
enemigos = []
vel_enemigos = 10
spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(spawn_event, 300)  # Cada segundo aparece enemigo

# Fuente
fuente = pygame.font.SysFont("Arial", 24)
score = 0

# Reloj
clock = pygame.time.Clock()

# Bucle del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == spawn_event:
            enemigo = pygame.Rect(ANCHO, random.randint(0, ALTO-40), 40, 40)
            enemigos.append(enemigo)

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP] and jugador.top > 0:
        jugador.y -= vel_jugador
        vel_jugador += 0.3
        if vel_jugador >= 10:
            vel_jugador = 10
    elif teclas[pygame.K_DOWN] and jugador.bottom < ALTO:
        jugador.y += vel_jugador
        vel_jugador += 0.3
        if vel_jugador >= 10:
            vel_jugador = 10
    else:
        vel_jugador = 5

    # Movimiento de enemigos
    for enemigo in enemigos[:]:
        enemigo.x -= vel_enemigos
        if enemigo.right < 0:
            enemigos.remove(enemigo)
            score += 1

    # Colisión
    for enemigo in enemigos:
        if jugador.colliderect(enemigo):
            VENTANA.fill(NEGRO)
            texto = fuente.render(f"¡Game Over! Puntaje: {score}", True, ROJO)
            VENTANA.blit(texto, (ANCHO//2 - texto.get_width()//2, ALTO//2))
            pygame.display.flip()
            pygame.time.delay(2000)
            pygame.quit()
            sys.exit()

    # Dibujar
    VENTANA.fill(BLANCO)
    pygame.draw.rect(VENTANA, AZUL, jugador)
    for enemigo in enemigos:
        pygame.draw.rect(VENTANA, ROJO, enemigo)

    # Mostrar puntaje
    texto = fuente.render(f"Puntaje: {score}", True, NEGRO)
    VENTANA.blit(texto, (10, 10))

    pygame.display.flip()
    clock.tick(60)
