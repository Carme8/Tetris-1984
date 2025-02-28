import pygame  # Importa la libreria Pygame per la grafica
from colors import Colors  # Importa il modulo Colors per ottenere i colori delle celle

class Grid:  # Definisce la classe Grid
    def __init__(self):  # Costruttore della classe Grid
        self.num_rows = 20  # Numero di righe della griglia
        self.num_cols = 10  # Numero di colonne della griglia
        self.cell_size = 30  # Dimensione di ogni cella
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]  # Crea una griglia 2D con valori iniziali 0
        self.colors = Colors.get_cell_colors()  # Ottiene i colori per le celle tramite il modulo Colors

    def print_grid(self):  # Stampa la griglia sulla console
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end=" ")  # Stampa il valore di ogni cella
            print()  # Vai a capo alla fine di ogni riga

    def is_inside(self, row, column):  # Verifica se una posizione è all'interno della griglia
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True  # La posizione è valida
        return False  # La posizione è fuori dalla griglia

    def is_empty(self, row, column):  # Verifica se una cella è vuota (valore 0)
        if self.grid[row][column] == 0:
            return True  # La cella è vuota
        return False  # La cella non è vuota

    def is_row_full(self, row):  # Verifica se una riga è piena (nessun valore 0)
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False  # La riga non è piena
        return True  # La riga è piena

    def clear_row(self, row):  # Pulisce una riga, impostando tutte le celle a 0
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    def move_row_down(self, row, num_rows):  # Muove una riga verso il basso di 'num_rows' posizioni
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]  # Sposta il valore
            self.grid[row][column] = 0  # Pulisce la riga originale

    def clear_full_rows(self):  # Elimina le righe piene e sposta le righe superiori verso il basso
        completed = 0  # Conta quante righe sono state completate
        for row in range(self.num_rows - 1, 0, -1):  # Inizia dalla fine della griglia
            if self.is_row_full(row):  # Se la riga è piena
                self.clear_row(row)  # Pulisci la riga
                completed += 1  # Incrementa il contatore
            elif completed > 0:  # Se ci sono righe completate
                self.move_row_down(row, completed)  # Muove le righe verso il basso
        return completed  # Restituisce il numero di righe eliminate

    def reset(self):  # Resetta la griglia (tutte le celle a 0)
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    def draw(self, screen):  # Disegna la griglia sullo schermo
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]  # Ottiene il valore della cella
                cell_rect = pygame.Rect(column * self.cell_size + 11, row * self.cell_size + 11, 
                                        self.cell_size - 1, self.cell_size - 1)  # Crea un rettangolo per la cella
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)  # Disegna il rettangolo con il colore associato

