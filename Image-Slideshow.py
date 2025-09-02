from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk
root = tk.Tk()
root.title("Image Slideshow Viewer")
#List of Image path
image_path = [
    r"C:\Users\Admin\Pictures\Screenshots\Screenshot (26).png",
    r"C:\Users\Admin\Pictures\Screenshots\Screenshot (27).png",
    r"C:\Users\Admin\Pictures\Screenshots\Screenshot (28).png",
    r"C:\Users\Admin\Pictures\Screenshots\Screenshot (29).png",
    r"C:\Users\Admin\Pictures\Screenshots\Screenshot (19).png",
]
#Resize the images to 1080x1080 
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_path]
photo_images = [ImageTk.PhotoImage(image) for image in images]
label = tk.Label(root)
label.pack()
def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)
slideshow = cycle(photo_images)
def start_slideshow():
    for _ in range(len(image_path)):
        update_image()
play_button = tk.Button(root, text='Play Slideshow', command=start_slideshow)
play_button.pack()
root.mainloop()