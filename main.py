import subprocess
import tkinter as tk
from PIL import ImageTk, Image

def run_file():
    subprocess.Popen(["python", "Volcontrol.py"])

root = tk.Tk()

root.title("My App")

bg_image = Image.open("Assets/bg.jpg")

bg_image = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_image)

bg_label.place(x=0, y=0, relwidth=1, relheight=1)

button = tk.Button(root, text="Run File", command=run_file)

button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def resize_bg(event):
    new_size = (event.width, event.height)
    bg_image_resized = bg_image.resize(new_size, Image.ANTIALIAS)
    bg_image_resized_tk = ImageTk.PhotoImage(bg_image_resized)
    bg_label.config(image=bg_image_resized_tk)
    bg_label.image = bg_image_resized_tk  

root.bind('<Configure>', resize_bg)

root.geometry("1200x800")

root.mainloop()