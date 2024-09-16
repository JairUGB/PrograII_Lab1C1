import tkinter as tk

# Función para crear la ventana
def crear_ventana():
    ventana = tk.Tk()  # Crear una ventana
    ventana.title("Datos Personales")  # Título de la ventana
    ventana.geometry("400x200")  # Tamaño de la ventana

    # Crear etiquetas para mostrar nombre y edad centrados
    etiqueta_nombre = tk.Label(ventana, text="Emerson Jair Umanzor Yanes", font=("Arial", 14))
    etiqueta_nombre.pack(pady=20)  # Empacar y añadir espacio vertical

    etiqueta_edad = tk.Label(ventana, text="Edad: 21 años", font=("Arial", 14))
    etiqueta_edad.pack(pady=20)  # Empacar y añadir espacio vertical

    ventana.mainloop()  # Iniciar el bucle principal de la ventana

# Llamar a la función para crear la ventana
crear_ventana()
