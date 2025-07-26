import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("win2")
ventana.geometry("300x150")

def saludo():
    messagebox.showinfo("Saludos", "Has pulsado el botón")

boton = tk.Button(ventana, text="Pulsa aquí", command=saludo, bg='green', fg='white')
boton.pack(pady=40)

ventana.mainloop()
