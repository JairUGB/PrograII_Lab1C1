import tkinter as tk
from tkinter import messagebox

# Función para manejar la lectura de la clave secreta
def leer_clave():
    clave = introducir_clave.get()  # Obtener el valor ingresado en la entrada
    messagebox.showinfo("Clave Secreta", "La clave ha sido ingresada exitosamente.")  # Mensaje de éxito
    introducir_clave.delete(0, tk.END)  # Limpiar el campo de la clave después de leerla

# Función para crear la ventana
def crear_ventana():
    ventana = tk.Tk()  # Crear una ventana
    ventana.title("Ingreso de Clave Secreta")  # Título de la ventana
    ventana.geometry("400x200")  # Tamaño de la ventana

    # Etiqueta para la clave secreta
    etiqueta_clave = tk.Label(ventana, text="Ingrese su clave ultra secreta:", font=("Arial", 14))
    etiqueta_clave.pack(pady=20)  # Empacar la etiqueta y añadir espacio vertical

    # Entrada para la clave secreta con los caracteres ocultos
    global introducir_clave
    introducir_clave = tk.Entry(ventana, font=("Arial", 14), show="*")
    introducir_clave.pack(pady=10)

    # Botón para leer la clave
    boton_leer = tk.Button(ventana, text="Ingresar", command=leer_clave, font=("Arial", 14))
    boton_leer.pack(pady=10)

    ventana.mainloop()  # Iniciar el bucle principal de la ventana

# Llamar a la función para crear la ventana
crear_ventana()
