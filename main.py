import pygame, sys  # Importa Pygame e il modulo sys per la gestione della chiusura
from game import Game  # Importa la classe Game che gestisce la logica del gioco
from colors import Colors  # Importa i colori definiti nel modulo Colors

pygame.init()  # Inizializza Pygame

# Creazione dei font e testi per l'interfaccia
title_font = pygame.font.Font("Tetris.ttf", 23)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

# Definizione delle aree per il punteggio e il prossimo pezzo
score_rect = pygame.Rect(320, 55, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

# Creazione della finestra di gioco
screen = pygame.display.set_mode((500, 620))
pygame.display.set_caption("Tetris 1984")

clock = pygame.time.Clock()  # Imposta il clock per limitare il frame rate
game = Game()  # Crea un'istanza del gioco

# Creazione di un evento personalizzato per aggiornare il gioco
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

# Loop principale del gioco
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Se l'utente chiude la finestra
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if game.game_over:  # Reset del gioco se è finito
                game.game_over = False
                game.reset()
            
            # Controlli della tastiera
            if event.key == pygame.K_LEFT and not game.game_over:
                game.move_left()
            if event.key == pygame.K_RIGHT and not game.game_over:
                game.move_right()
            if event.key == pygame.K_DOWN and not game.game_over:
                game.move_down()
                game.update_score(0, 1)
            if event.key == pygame.K_UP and not game.game_over:
                game.rotate()
        
        if event.type == GAME_UPDATE and not game.game_over:
            game.move_down()  # Fa scendere il pezzo automaticamente

    # Aggiornamento interfaccia grafica
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    screen.fill(Colors.dark_gray)  # Sfondo grigio scuro
    screen.blit(score_surface, (365, 20))
    screen.blit(next_surface, (375, 180))

    if game.game_over:
        screen.blit(game_over_surface, (320, 450))  # Mostra "GAME OVER" se il gioco è finito
    
    # Disegna i riquadri del punteggio e del prossimo pezzo
    pygame.draw.rect(screen, Colors.black, score_rect, 0, 10)
    screen.blit(score_value_surface, score_value_surface.get_rect(center=score_rect.center))
    pygame.draw.rect(screen, Colors.black, next_rect, 0, 10)
    
    game.draw(screen)  # Disegna il gioco
    pygame.display.update()  # Aggiorna lo schermo
    clock.tick(60)  # Limita il frame rate a 60 FPS
