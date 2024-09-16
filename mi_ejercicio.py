# Este programa en PyQt crea una interfaz gráfica que permite ingresar y visualizar datos personales de manera estructurada, 
# como el nombre, género, país de origen, nivel educativo y número de hijos, utilizando widgets como QRadioButton, QComboBox y 
# QSpinBox para facilitar la interacción del usuario. Resuelve el problema de la recolección de información al ofrecer un método 
# intuitivo y libre de errores, donde los datos predefinidos y opciones seleccionables eliminan la posibilidad de entradas incorrectas, 
# siendo útil en situaciones como formularios de registro o encuestas en aplicaciones de escritorio.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QRadioButton, QVBoxLayout, QComboBox, QSpinBox, QPushButton, QMessageBox

class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configuración de la ventana
        self.setWindowTitle('Datos Personales')
        self.setGeometry(100, 100, 400, 400)

        # Crear layout principal
        layout = QVBoxLayout()

        # Etiqueta y campo de texto para el nombre
        self.label_nombre = QLabel('Nombre:')
        self.input_nombre = QLineEdit(self)
        layout.addWidget(self.label_nombre)
        layout.addWidget(self.input_nombre)

        # Radiobuttons para seleccionar el género
        self.label_genero = QLabel('Género:')
        self.radio_hombre = QRadioButton('Hombre', self)
        self.radio_mujer = QRadioButton('Mujer', self)
        layout.addWidget(self.label_genero)
        layout.addWidget(self.radio_hombre)
        layout.addWidget(self.radio_mujer)

        # Combobox para seleccionar el país de origen
        self.label_pais = QLabel('País de Origen:')
        self.combo_pais = QComboBox(self)
        self.combo_pais.addItems([
            'El Salvador', 'México', 'Guatemala', 'Honduras', 'Costa Rica',
            'Panamá', 'Colombia', 'Argentina', 'España', 'Estados Unidos'
        ])
        layout.addWidget(self.label_pais)
        layout.addWidget(self.combo_pais)

        # Combobox para seleccionar el nivel educativo
        self.label_educacion = QLabel('Nivel de Educación:')
        self.combo_educacion = QComboBox(self)
        self.combo_educacion.addItems(['Primaria', 'Secundaria', 'Universidad', 'Postgrado'])
        layout.addWidget(self.label_educacion)
        layout.addWidget(self.combo_educacion)

        # Spinbox para seleccionar el número de hijos
        self.label_hijos = QLabel('Número de hijos:')
        self.spin_hijos = QSpinBox(self)
        self.spin_hijos.setRange(0, 10)  # Rango entre 0 y 10 hijos
        layout.addWidget(self.label_hijos)
        layout.addWidget(self.spin_hijos)

        # Botón para enviar los datos
        self.boton_enviar = QPushButton('Enviar', self)
        self.boton_enviar.clicked.connect(self.mostrar_datos)
        layout.addWidget(self.boton_enviar)

        # Establecer el layout
        self.setLayout(layout)

    def mostrar_datos(self):
        # Obtener el nombre
        nombre = self.input_nombre.text()

        # Obtener el género
        if self.radio_hombre.isChecked():
            genero = 'Hombre'
        elif self.radio_mujer.isChecked():
            genero = 'Mujer'
        else:
            genero = 'No especificado'

        # Obtener el país de origen
        pais_origen = self.combo_pais.currentText()

        # Obtener el nivel educativo
        educacion = self.combo_educacion.currentText()

        # Obtener el número de hijos
        hijos = self.spin_hijos.value()

        # Mostrar los datos en un mensaje
        mensaje = (f"Nombre: {nombre}\n"
                   f"Género: {genero}\n"
                   f"País de Origen: {pais_origen}\n"
                   f"Educación: {educacion}\n"
                   f"Número de hijos: {hijos}")
        QMessageBox.information(self, 'Datos Ingresados', mensaje)

# Función principal para ejecutar la aplicación
def main():
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()