import tkinter as tk
from tkinter import messagebox

# Función para leer los datos ingresados
def leer_datos():
    nombre = entrada_nombre.get()  # Obtener el nombre ingresado
    cedula = entrada_cedula.get()  # Obtener la cédula ingresada
    if nombre and cedula:
        mensaje = f"Nombre: {nombre}\nCédula: {cedula}"
        messagebox.showinfo("Datos Ingresados", mensaje)  # Mostrar los datos ingresados en un mensaje
        entrada_nombre.delete(0, tk.END)  # Limpiar el campo de nombre
        entrada_cedula.delete(0, tk.END)  # Limpiar el campo de cédula
    else:
        messagebox.showwarning("Error", "Por favor, complete ambos campos.")  # Avisar si hay campos vacíos

# Función para crear la ventana
def crear_ventana():
    ventana = tk.Tk()  # Crear una ventana
    ventana.title("Ingreso de Datos Personales")  # Título de la ventana
    ventana.geometry("400x300")  # Tamaño de la ventana

    # Etiqueta para el nombre completo
    etiqueta_nombre = tk.Label(ventana, text="Ingrese su nombre completo:", font=("Arial", 14))
    etiqueta_nombre.pack(pady=10)  # Empacar la etiqueta con espacio vertical

    # Campo de entrada para el nombre completo
    global entrada_nombre
    entrada_nombre = tk.Entry(ventana, font=("Arial", 14))
    entrada_nombre.pack(pady=10)

    # Etiqueta para el número de cédula
    etiqueta_cedula = tk.Label(ventana, text="Ingrese su número de cédula:", font=("Arial", 14))
    etiqueta_cedula.pack(pady=10)

    # Campo de entrada para el número de cédula
    global entrada_cedula
    entrada_cedula = tk.Entry(ventana, font=("Arial", 14))
    entrada_cedula.pack(pady=10)

    # Botón para leer los datos
    boton_leer = tk.Button(ventana, text="Ingresar", command=leer_datos, font=("Arial", 14))
    boton_leer.pack(pady=20)

    ventana.mainloop()  # Iniciar el bucle principal de la ventana

# Llamar a la función para crear la ventana
crear_ventana()
