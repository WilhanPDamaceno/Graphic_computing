import tkinter as tk

def create_board():
    window = tk.Tk()
    window.title("Tabuleiro de Damas")

    canvas = tk.Canvas(window, width=400, height=400, bg="lightgray")
    canvas.pack()

    square_size = 50
    for row in range(8):
        for col in range(8):
            x1 = col * square_size
            y1 = row * square_size
            x2 = x1 + square_size
            y2 = y1 + square_size
            color = "white" if (row + col) % 2 == 0 else "black"
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")
    piece_radius = (square_size / 2) - 5
    for row in range(8):
        for col in range(8):
            if (row + col) % 2 != 0:  # Apenas em casas escuras
                center_x = col * square_size + square_size / 2
                center_y = row * square_size + square_size / 2
                
                if row < 3:  # Peças brancas nas 3 primeiras linhas
                    canvas.create_oval(center_x - piece_radius, center_y - piece_radius, 
                                       center_x + piece_radius, center_y + piece_radius, 
                                       fill="red", outline="darkred")
                elif row > 4:  # Peças pretas nas 3 últimas linhas
                    canvas.create_oval(center_x - piece_radius, center_y - piece_radius, 
                                       center_x + piece_radius, center_y + piece_radius, 
                                       fill="blue", outline="darkblue")

    window.mainloop()

if __name__ == "__main__":
    create_board()