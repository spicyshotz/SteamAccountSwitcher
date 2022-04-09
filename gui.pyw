from pathlib import Path
import os
from pynput.keyboard import Key, Listener
import json


from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

f = open('curacc.json')
data = json.load(f)
curacc = data["acc"]
f.close()

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_main():
    global curacc
    global data
    os.popen('main.bat')
    if curacc == '2':
        data["acc"] = '1'
    with open('curacc.json', 'w') as json_file:
        json.dump(data, json_file)
    window.destroy()

def open_alt():
    global curacc
    global data
    os.popen('alt.bat')
    if curacc == '1':
        data["acc"] = '2'
    with open('curacc.json', 'w') as json_file:
        json.dump(data, json_file)
    window.destroy()

window = Tk()
window.title('Steam Account Switcher')
window.iconbitmap(relative_to_assets("steam.ico"))

window.geometry("700x500")
window.configure(bg = "#1B2838")


canvas = Canvas(
    window,
    bg = "#1B2838",
    height = 500,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
if curacc == '2':
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
else:
    button_image_1 = PhotoImage(
    file=relative_to_assets("button_1_selected.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=open_main,
    relief="flat"
)
button_1.place(
    x=82.99999999999994,
    y=109.0,
    width=207.0,
    height=207.0
)
if curacc == '1':
    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
else:
    button_image_2 = PhotoImage(
    file=relative_to_assets("button_2_selected.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=open_alt,
    relief="flat"
)
button_2.place(
    x=409.99999999999994,
    y=109.0,
    width=207.0,
    height=207.0
)

canvas.create_text(
    448.99999999999994,
    328.0,
    anchor="nw",
    text="Alt Account",
    fill="#FFFFFF",
    font=("RobotoSlab Regular", 24 * -1)
)

canvas.create_text(
    105.99999999999994,
    328.0,
    anchor="nw",
    text="Main Account",
    fill="#FFFFFF",
    font=("RobotoSlab Regular", 24 * -1)
)

canvas.create_text(
    236.99999999999994,
    459.0,
    anchor="nw",
    text="Pro tip: press 1 / 2 for quick switch",
    fill="#3C5069",
    font=("RobotoFlex Regular", 15 * -1)
)

canvas.create_text(
    303.99999999999994,
    482.0,
    anchor="nw",
    text="Made by Spicyshotz",
    fill="#3C5069",
    font=("RobotoFlex Regular", 10 * -1)
)

canvas.create_text(
    181.99999999999994,
    372.0,
    anchor="nw",
    text="1",
    fill="#3C5069",
    font=("RobotoFlex Regular", 15 * -1)
)

canvas.create_text(
    508.99999999999994,
    372.0,
    anchor="nw",
    text="2",
    fill="#3C5069",
    font=("RobotoFlex Regular", 15 * -1)
)

def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

def key_pressed(event):
    if event.char == '1':
       open_main()
    if event.char == '2':
       open_alt()
window.bind("<Key>",key_pressed)
center(window)
#window.overrideredirect(True)
window.resizable(False, False)
window.mainloop()
