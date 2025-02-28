from colors import Colors  # Importa il modulo Colors per ottenere i colori delle celle
import pygame  # Importa Pygame per la grafica
from position import Position  # Importa la classe Position per gestire le posizioni delle celle

class Block:  # Definisce la classe Block per rappresentare un blocco
    def __init__(self, id):  # Costruttore della classe Block
        self.id = id  # Identificatore del blocco (ad esempio, per il colore)
        self.cells = {}  # Dizionario che contiene le posizioni delle celle per ogni stato di rotazione
        self.cell_size = 30  # Dimensione di ogni cella
        self.row_offset = 0  # Offset delle righe (per spostare il blocco nella griglia)
        self.column_offset = 0  # Offset delle colonne (per spostare il blocco nella griglia)
        self.rotation_state = 0  # Stato di rotazione del blocco (0, 1, 2, 3)
        self.colors = Colors.get_cell_colors()  # Ottiene i colori delle celle tramite Colors

    def move(self, rows, columns):  # Muove il blocco nella griglia di un certo numero di righe e colonne
        self.row_offset += rows  # Aggiunge l'offset delle righe
        self.column_offset += columns  # Aggiunge l'offset delle colonne

    def get_cell_positions(self):  # Restituisce le posizioni delle celle del blocco (tenendo conto degli offset)
        tiles = self.cells[self.rotation_state]  # Ottiene le posizioni delle celle per lo stato di rotazione corrente
        moved_tiles = []  # Lista per le posizioni modificate
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)  # Aggiunge gli offset
            moved_tiles.append(position)  # Aggiunge la posizione spostata alla lista
        return moved_tiles  # Restituisce le posizioni delle celle modificate

    def rotate(self):  # Ruota il blocco di 90 gradi (passa al prossimo stato di rotazione)
        self.rotation_state += 1  # Aumenta lo stato di rotazione
        if self.rotation_state == len(self.cells):  # Se si supera il numero massimo di stati, torna allo stato iniziale
            self.rotation_state = 0

    def undo_rotation(self):  # Annulla la rotazione (torna allo stato precedente)
        self.rotation_state -= 1  # Diminuisce lo stato di rotazione
        if self.rotation_state == -1:  # Se si è già al primo stato, passa all'ultimo
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):  # Disegna il blocco sullo schermo
        tiles = self.get_cell_positions()  # Ottiene le posizioni delle celle del blocco
        for tile in tiles:  # Per ogni cella
            tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,  # Crea un rettangolo per la cella
                                    offset_y + tile.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)  # Disegna il rettangolo con il colore del blocco

