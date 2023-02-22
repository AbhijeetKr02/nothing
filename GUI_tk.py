#GUI using tkinter interface
import tkinter as tk

root = tk.Tk()
root.title("Simple GUI")

label = tk.Label(root, text="Hello, World!")
label.pack()

button = tk.Button(root, text="Click me", command=root.destroy)
button.pack()

root.mainloop()