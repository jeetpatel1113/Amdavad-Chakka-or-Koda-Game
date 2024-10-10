from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import time
from random import randint, choice

class Amdavad:
    def __init__(self, root, white_face, black_face):
        self.window = root
        #Make canvas
        self.make_canvas = Canvas(self.window, bg = "#111111", width = 800, height= 600)
        self.make_canvas.pack(fill=BOTH, expand=1)
        
        # Make some containers to store data
        self.make_red_coin = []
        self.make_green_coin = []
        self.make_yellow_coin = []
        self.make_blue_coin = []
        
        self.make_red_label = []
        self.make__green_label = []
        self.make_yellow_label = []
        self.make_blue_label = []
        
        self.block_value_predict = []
        self.total_people_play = []
        
        # Ludo block all side image store
        self.block_value_side = [white_face, black_face]
        
        # Use for store specific position of all coins
        self.red_coord_store = [-1, -1, -1, -1]
        self.green_coord_store = [-1, -1, -1, -1]
        self.yellow_coord_store = [-1, -1, -1, -1]
        self.blue_coord_store = [-1, -1, -1, -1]
        
        self.red_coin_position = [0, 1, 2, 3]
        self.green_coin_position = [0, 1, 2, 3]
        self.yellow_coin_position = [0, 1, 2, 3]
        self.blue_coin_position = [0, 1, 2, 3]
        
        
        
        

if __name__ == '__main__':
    window = Tk()
    window.geometry("800x600")
    main_canvas_x = 800
    main_canvas_y = 600
    window.maxsize(main_canvas_x,main_canvas_y)
    window.minsize(main_canvas_x,main_canvas_y)
    window.title("Welcome to the Game of Amdavad!")
    
    # Add an icon for the application
    # window.iconbitmap("Images/ludo_icon.ico")
    
    # Dice images, there will be 2 facings
    chakka_x = main_canvas_x / 64
    chakka_y = main_canvas_y / 8
    
    white_face = ImageTk.PhotoImage((Image.open("Images/chakka_white_face.png")).resize((int(chakka_x), int(chakka_y)), Image.LANCZOS))
    black_face = ImageTk.PhotoImage(Image.open("Images/chakka_black_face.png").resize((int(chakka_x), int(chakka_y)), Image.LANCZOS))
    
    
    temp = Label(window,image=white_face)
    temp.place(x=34,y=15)
    temp = Label(window,image=black_face)
    temp.place(x=100,y=15)
    # Ludo(window,block_six_side,block_five_side,block_four_side,block_three_side,block_two_side,block_one_side)
    
    Amdavad(window, white_face, black_face)
    window.mainloop()