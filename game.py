from grid import Grid  # Importa la classe Grid per gestire la griglia
from blocks import *  # Importa tutte le classi dei blocchi
import random  # Importa il modulo random per generare blocchi casuali
import pygame  # Importa Pygame per la gestione della grafica e suoni

class Game:  # Definisce la classe Game per gestire la logica del gioco
    def __init__(self):  # Costruttore della classe Game
        self.grid = Grid()  # Crea una nuova griglia di gioco
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Lista di blocchi disponibili
        self.current_block = self.get_random_block()  # Assegna un blocco casuale come blocco attivo
        self.next_block = self.get_random_block()  # Assegna un blocco casuale come prossimo blocco
        self.game_over = False  # Inizializza lo stato del gioco come non finito
        self.score = 0  # Imposta il punteggio iniziale a 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")  # Carica il suono di rotazione
        self.clear_sound = pygame.mixer.Sound("Sounds/clear.ogg")  # Carica il suono di eliminazione righe

        pygame.mixer.music.load("Sounds/music.ogg")  # Carica la musica di sottofondo
        pygame.mixer.music.play(-1)  # Riproduce la musica in loop

    def update_score(self, lines_cleared, move_down_points):  # Aggiorna il punteggio in base alle righe eliminate
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points  # Aggiunge i punti per il movimento verso il basso

    def get_random_block(self):  # Restituisce un blocco casuale
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]  # Ristabilisce la lista di blocchi
        block = random.choice(self.blocks)  # Seleziona un blocco casuale
        self.blocks.remove(block)  # Rimuove il blocco dalla lista
        return block

    def move_left(self):  # Muove il blocco attivo a sinistra
        self.current_block.move(0, -1)
        if not self.block_inside() or not self.block_fits():  # Controlla se il movimento è valido
            self.current_block.move(0, 1)  # Se non valido, annulla il movimento

    def move_right(self):  # Muove il blocco attivo a destra
        self.current_block.move(0, 1)
        if not self.block_inside() or not self.block_fits():  # Controlla se il movimento è valido
            self.current_block.move(0, -1)  # Se non valido, annulla il movimento

    def move_down(self):  # Muove il blocco attivo verso il basso
        self.current_block.move(1, 0)
        if not self.block_inside() or not self.block_fits():  # Controlla se il movimento è valido
            self.current_block.move(-1, 0)  # Se non valido, annulla il movimento
            self.lock_block()  # Blocca il blocco nella griglia

    def lock_block(self):  # Blocca il blocco nella griglia
        tiles = self.current_block.get_cell_positions()  # Ottiene le posizioni delle celle del blocco
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id  # Assegna il blocco alla griglia
        self.current_block = self.next_block  # Imposta il prossimo blocco come blocco attivo
        self.next_block = self.get_random_block()  # Ottiene un nuovo blocco per il prossimo turno
        rows_cleared = self.grid.clear_full_rows()  # Pulisce le righe complete
        if rows_cleared > 0:
            self.clear_sound.play()  # Suona il suono di eliminazione righe
            self.update_score(rows_cleared, 0)  # Aggiorna il punteggio
        if not self.block_fits():  # Se il blocco non può essere inserito, finisce il gioco
            self.game_over = True

    def reset(self):  # Resetta il gioco, ripristinando la griglia e il punteggio
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0

    def block_fits(self):  # Controlla se il blocco attivo può essere posizionato nella griglia
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_empty(tile.row, tile.column):  # Se una cella non è vuota, il blocco non può entrare
                return False
        return True  # Il blocco si adatta se tutte le celle sono vuote

    def rotate(self):  # Ruota il blocco attivo
        self.current_block.rotate()
        if not self.block_inside() or not self.block_fits():  # Se la rotazione non è valida
            self.current_block.undo_rotation()  # Annulla la rotazione
        else:
            self.rotate_sound.play()  # Suona il suono di rotazione

    def block_inside(self):  # Controlla se il blocco attivo è all'interno dei confini della griglia
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if not self.grid.is_inside(tile.row, tile.column):  # Se una cella è fuori dalla griglia
                return False
        return True  # Il blocco è all'interno se tutte le celle sono valide

    def draw(self, screen):  # Disegna la griglia e i blocchi sullo schermo
        self.grid.draw(screen)  # Disegna la griglia
        self.current_block.draw(screen, 11, 11)  # Disegna il blocco attivo

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)  # Disegna il prossimo blocco
