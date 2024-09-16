import tkinter as tk
from tkinter import messagebox

# Función para leer los datos ingresados de las mascotas
def leer_datos():
    mascota1 = (entrada_nombre1.get(), entrada_tipo1.get(), entrada_edad1.get())
    mascota2 = (entrada_nombre2.get(), entrada_tipo2.get(), entrada_edad2.get())
    mascota3 = (entrada_nombre3.get(), entrada_tipo3.get(), entrada_edad3.get())

    # Validar que todos los campos estén llenos
    if all(mascota1) and all(mascota2) and all(mascota3):
        mensaje = (f"--- Mascota 1 ---\nNombre: {mascota1[0]}\nTipo: {mascota1[1]}\nEdad: {mascota1[2]} años\n\n"
                   f"--- Mascota 2 ---\nNombre: {mascota2[0]}\nTipo: {mascota2[1]}\nEdad: {mascota2[2]} años\n\n"
                   f"--- Mascota 3 ---\nNombre: {mascota3[0]}\nTipo: {mascota3[1]}\nEdad: {mascota3[2]} años")
        messagebox.showinfo("Datos de las Mascotas", mensaje)  # Mostrar los datos de las mascotas
        limpiar_campos()  # Limpiar los campos después de leer los datos
    else:
        messagebox.showwarning("Error", "Por favor, complete todos los campos de las tres mascotas.")  # Avisar si faltan datos

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_nombre1.delete(0, tk.END)
    entrada_tipo1.delete(0, tk.END)
    entrada_edad1.delete(0, tk.END)
    entrada_nombre2.delete(0, tk.END)
    entrada_tipo2.delete(0, tk.END)
    entrada_edad2.delete(0, tk.END)
    entrada_nombre3.delete(0, tk.END)
    entrada_tipo3.delete(0, tk.END)
    entrada_edad3.delete(0, tk.END)

# Función para crear la ventana
def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Datos de Mascotas")
    ventana.geometry("700x700")

    # Datos de la primera mascota
    tk.Label(ventana, text="Mascota 1", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(ventana, text="Nombre:").pack()
    global entrada_nombre1
    entrada_nombre1 = tk.Entry(ventana)
    entrada_nombre1.pack()

    tk.Label(ventana, text="Tipo:").pack()
    global entrada_tipo1
    entrada_tipo1 = tk.Entry(ventana)
    entrada_tipo1.pack()

    tk.Label(ventana, text="Edad:").pack()
    global entrada_edad1
    entrada_edad1 = tk.Entry(ventana)
    entrada_edad1.pack()

    # Datos de la segunda mascota
    tk.Label(ventana, text="Mascota 2", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(ventana, text="Nombre:").pack()
    global entrada_nombre2
    entrada_nombre2 = tk.Entry(ventana)
    entrada_nombre2.pack()

    tk.Label(ventana, text="Tipo:").pack()
    global entrada_tipo2
    entrada_tipo2 = tk.Entry(ventana)
    entrada_tipo2.pack()

    tk.Label(ventana, text="Edad:").pack()
    global entrada_edad2
    entrada_edad2 = tk.Entry(ventana)
    entrada_edad2.pack()

    # Datos de la tercera mascota
    tk.Label(ventana, text="Mascota 3", font=("Arial", 12, "bold")).pack(pady=10)
    tk.Label(ventana, text="Nombre:").pack()
    global entrada_nombre3
    entrada_nombre3 = tk.Entry(ventana)
    entrada_nombre3.pack()

    tk.Label(ventana, text="Tipo:").pack()
    global entrada_tipo3
    entrada_tipo3 = tk.Entry(ventana)
    entrada_tipo3.pack()

    tk.Label(ventana, text="Edad:").pack()
    global entrada_edad3
    entrada_edad3 = tk.Entry(ventana)
    entrada_edad3.pack()

    # Botón para leer los datos
    boton_leer = tk.Button(ventana, text="Ingresar", command=leer_datos, font=("Arial", 12))
    boton_leer.pack(pady=20)

    ventana.mainloop()

# Llamar a la función para crear la ventana
crear_ventana()

