import tkinter as tk
from tkinter import messagebox

# Función para leer los datos ingresados
def leer_datos():
    datos = {
        'Nombre': entrada_nombre.get(),
        'Edad': entrada_edad.get(),
        'Dirección': entrada_direccion.get(),
        'Teléfono': entrada_telefono.get(),
        'Correo Electrónico': entrada_correo.get(),
        'Fecha de Nacimiento': entrada_fecha_nacimiento.get(),
        'Sexo': entrada_sexo.get(),
        'Nacionalidad': entrada_nacionalidad.get(),
        'Ocupación': entrada_ocupacion.get(),
        'Estado Civil': entrada_estado_civil.get()
    }

    # Validar que todos los campos estén llenos
    if all(datos.values()):
        mensaje = "\n".join([f"{key}: {value}" for key, value in datos.items()])
        messagebox.showinfo("Datos Ingresados", mensaje)  # Mostrar los datos en un mensaje
        limpiar_campos()  # Limpiar los campos después de leer los datos
    else:
        messagebox.showwarning("Error", "Por favor, complete todos los campos.")  # Avisar si faltan datos

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_nombre.delete(0, tk.END)
    entrada_edad.delete(0, tk.END)
    entrada_direccion.delete(0, tk.END)
    entrada_telefono.delete(0, tk.END)
    entrada_correo.delete(0, tk.END)
    entrada_fecha_nacimiento.delete(0, tk.END)
    entrada_sexo.delete(0, tk.END)
    entrada_nacionalidad.delete(0, tk.END)
    entrada_ocupacion.delete(0, tk.END)
    entrada_estado_civil.delete(0, tk.END)

# Función para crear la ventana
def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ingreso de Datos Personales")
    ventana.geometry("600x400")

    # Crear una cuadrícula para organizar los widgets
    ventana.grid_columnconfigure(1, weight=1)  # Configurar la columna 1 para que se expanda
    ventana.grid_rowconfigure(list(range(10)), weight=1)  # Configurar todas las filas para que se expandan

    # Campos para ingresar datos
    campos = [
        ("Nombre:", "Nombre"),
        ("Edad:", "Edad"),
        ("Dirección:", "Dirección"),
        ("Teléfono:", "Teléfono"),
        ("Correo Electrónico:", "Correo Electrónico"),
        ("Fecha de Nacimiento:", "Fecha de Nacimiento"),
        ("Sexo:", "Sexo"),
        ("Nacionalidad:", "Nacionalidad"),
        ("Ocupación:", "Ocupación"),
        ("Estado Civil:", "Estado Civil")
    ]

    global entrada_nombre, entrada_edad, entrada_direccion, entrada_telefono, entrada_correo
    global entrada_fecha_nacimiento, entrada_sexo, entrada_nacionalidad, entrada_ocupacion, entrada_estado_civil

    for i, (etiqueta, _) in enumerate(campos):
        tk.Label(ventana, text=etiqueta, font=("Arial", 12)).grid(row=i, column=0, sticky='e', padx=10, pady=5)
        if i == 0:
            entrada_nombre = tk.Entry(ventana, font=("Arial", 12))
            entrada_nombre.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 1:
            entrada_edad = tk.Entry(ventana, font=("Arial", 12))
            entrada_edad.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 2:
            entrada_direccion = tk.Entry(ventana, font=("Arial", 12))
            entrada_direccion.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 3:
            entrada_telefono = tk.Entry(ventana, font=("Arial", 12))
            entrada_telefono.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 4:
            entrada_correo = tk.Entry(ventana, font=("Arial", 12))
            entrada_correo.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 5:
            entrada_fecha_nacimiento = tk.Entry(ventana, font=("Arial", 12))
            entrada_fecha_nacimiento.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 6:
            entrada_sexo = tk.Entry(ventana, font=("Arial", 12))
            entrada_sexo.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 7:
            entrada_nacionalidad = tk.Entry(ventana, font=("Arial", 12))
            entrada_nacionalidad.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 8:
            entrada_ocupacion = tk.Entry(ventana, font=("Arial", 12))
            entrada_ocupacion.grid(row=i, column=1, sticky='w', padx=10, pady=5)
        elif i == 9:
            entrada_estado_civil = tk.Entry(ventana, font=("Arial", 12))
            entrada_estado_civil.grid(row=i, column=1, sticky='w', padx=10, pady=5)

    # Botón para leer los datos
    boton_leer = tk.Button(ventana, text="Ingresar", command=leer_datos, font=("Arial", 12))
    boton_leer.grid(row=10, column=0, columnspan=2, pady=20)

    ventana.mainloop()

# Llamar a la función para crear la ventana
crear_ventana()
